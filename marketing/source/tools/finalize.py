"""Create and validate print / interactive editions after tools/render.cjs."""
from pathlib import Path
from collections import Counter
import argparse,json,re,shutil
import pymupdf as fitz
from pypdf import PdfReader,PdfWriter
from pypdf.generic import DictionaryObject,NameObject,TextStringObject
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--build-dir',type=Path,default=root/'rebuilt');args=parser.parse_args()
out=args.build_dir.resolve();scratch=out/'.render'
tokens=lambda s:Counter(re.findall('[a-z0-9]+',s.lower()))
def owner(widget):
 while '/T' not in widget and '/Parent' in widget:widget=widget['/Parent'].get_object()
 return widget
def make_print(src,dst):
 writer=PdfWriter();writer.clone_document_from_reader(PdfReader(src))
 values={k:f.get('/V','/Off' if f.get('/FT')=='/Btn' else '') for k,f in (writer.get_fields() or {}).items()}
 populated={k:v for k,v in values.items() if str(v) not in ('','/Off','Off')}
 if populated:writer.update_page_form_field_values(None,populated,auto_regenerate=False,flatten=True)
 writer.remove_annotations(subtypes='/Widget');writer._root_object.pop('/AcroForm',None);writer.write(dst)
 check=PdfReader(dst);assert not check.get_fields()
 assert all(ref.get_object().get('/Subtype')!='/Widget' for p in check.pages for ref in p.get('/Annots',[]))
for c in json.loads((root/'documents.json').read_text(encoding='utf8')):
 id=c['id'];raw=scratch/(id+'.pdf');doc=fitz.open(raw)
 expected=json.loads((root/'06_Release_Data'/(id+'-text.json')).read_text(encoding='utf8'))
 assert len(doc)==c['pages']==len(expected),(id,'Page count changed')
 for n,p in enumerate(doc):assert tokens(p.get_text())==tokens(expected[n]),(id,n+1,'Text changed')
 fields=json.loads((scratch/(id+'-fields.json')).read_text(encoding='utf8'));spec=json.loads((root/'06_Release_Data'/(id+'-fields.json')).read_text(encoding='utf8'))
 assert len(fields)==c['fields']==len(spec)
 assert {f['name'] for f in fields}==set(spec)
 printfile=out/(c['title']+'.pdf')
 if not fields:shutil.copy2(raw,printfile);doc.close();print(id+': print edition verified');continue
 for f in fields:
  previous=spec[f['name']];w=fitz.Widget();w.field_name=f['name'];w.rect=fitz.Rect(f['x']*.75,f['y']*.75,(f['x']+f['w'])*.75,(f['y']+f['h'])*.75);w.border_width=0;w.text_color=(.102,.196,.49);w.field_flags=previous['flags']
  if previous['type']=='/Btn':w.field_type=fitz.PDF_WIDGET_TYPE_CHECKBOX;w.field_value=previous['value'].lstrip('/')
  else:w.field_type=fitz.PDF_WIDGET_TYPE_TEXT;w.field_value=previous['value'];w.text_font='Helv';w.text_fontsize=9 if f['type']=='multi' else 0
  doc[f['page']].add_widget(w)
 intermediate=scratch/(id+'-widgets.pdf');doc.save(intermediate,garbage=3,deflate=True);doc.close()
 writer=PdfWriter();writer.clone_document_from_reader(PdfReader(intermediate));acro=writer._root_object['/AcroForm']
 resources=acro.get('/DR',DictionaryObject());fonts=resources.get('/Font',DictionaryObject())
 helvetica=DictionaryObject({NameObject('/Type'):NameObject('/Font'),NameObject('/Subtype'):NameObject('/Type1'),NameObject('/BaseFont'):NameObject('/Helvetica'),NameObject('/Encoding'):NameObject('/WinAnsiEncoding')})
 fonts[NameObject('/Helv')]=writer._add_object(helvetica);resources[NameObject('/Font')]=fonts;acro[NameObject('/DR')]=resources;acro[NameObject('/DA')]=TextStringObject('/Helv 0 Tf 0.102 0.196 0.49 rg')
 folder=out/'Fillable';folder.mkdir(exist_ok=True);fillable=folder/(c['title']+' - FILLABLE.pdf');writer.write(fillable)
 reader=PdfReader(fillable);canonical=reader.get_fields();assert set(canonical)==set(spec)
 widgets=[]
 for page in reader.pages:
  for ref in page.get('/Annots',[]):
   widget=ref.get_object()
   if widget.get('/Subtype')!='/Widget':continue
   field=owner(widget);name=str(field['/T']);assert name in canonical
   assert str(field.get('/V',''))==str(canonical[name].get('/V',''))
   assert widget.get('/AP') and widget['/AP'].get('/N');widgets.append(widget)
 assert len(widgets)==c['fields']
 # Fill a text field on each applicable page and a checkbox, save, reopen, check canonical values.
 sample_values={}
 for page in reader.pages:
  for ref in page.get('/Annots',[]):
   field=owner(ref.get_object())
   if field.get('/FT')=='/Tx':sample_values[str(field['/T'])]='QA SAMPLE';break
 for widget in widgets:
  field=owner(widget)
  if field.get('/FT')=='/Btn':
   state=next(k for k in widget['/AP']['/N'] if str(k)!='/Off');sample_values[str(field['/T'])]=state;break
 test=PdfWriter();test.clone_document_from_reader(reader);test.update_page_form_field_values(None,sample_values,auto_regenerate=False);sample=scratch/(id+'-fill-test.pdf');test.write(sample)
 reopened=PdfReader(sample).get_fields()
 for name,value in sample_values.items():assert str(reopened[name].get('/V'))==str(value),(id,name,'Sample fill failed')
 make_print(fillable,printfile)
 print(id+': print + '+str(c['fields'])+' interactive fields verified; sample fill passed')
