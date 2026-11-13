"""Build private installable ZIPs from this isolated project. No external deps."""
from pathlib import Path
import hashlib,json,zipfile,tempfile,subprocess
ROOT=Path(__file__).resolve().parent.parent
PLUGIN=ROOT/'plugin';SKILL=PLUGIN/'skills/gcpro-accounting';DIST=ROOT/'dist'
PIN='8D461CB3189DFEE5C12373642DDBE8009151C9969551C352980D0439C0F03948'
def sha(b):return hashlib.sha256(b).hexdigest().upper()
def paths(root):return sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())
def write_manifest(root):
 files=[p for p in paths(root) if p!='package-manifest.sha256']
 (root/'package-manifest.sha256').write_text(''.join(sha((root/f).read_bytes())+'  '+f+'\n' for f in files),encoding='ascii',newline='\n')
def verify_manifest(root):
 seen=set()
 for line in (root/'package-manifest.sha256').read_text().splitlines():
  digest,file=line.split('  ',1)
  assert file not in seen and not Path(file).is_absolute() and '..' not in Path(file).parts
  assert sha((root/file).read_bytes())==digest,file
  seen.add(file)
 assert seen==set(paths(root))-{'package-manifest.sha256'}
assert sha((SKILL/'engine/scripts/dist/run-gas-report.mjs').read_bytes())==PIN
write_manifest(SKILL);write_manifest(PLUGIN);DIST.mkdir(exist_ok=True)
def build(source,name,prefix):
 target=DIST/name;files=paths(source)
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
  for f in files:
   assert not any(x in {'auth.json','.env','.git','node_modules','private-validation','private-inputs'} for x in Path(f).parts)
   assert not f.lower().endswith(('.csv','.xls','.xlsx','.xlsm','.zip'))
   assert not (source/f).is_symlink()
   i=zipfile.ZipInfo(prefix+f,(2026,11,13,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o100644<<16;z.writestr(i,(source/f).read_bytes())
 with tempfile.TemporaryDirectory(prefix='gcpro-accounting-install-') as tmp:
  with zipfile.ZipFile(target) as z:
   assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()));z.extractall(tmp)
  installed=Path(tmp)/prefix;verify_manifest(installed)
  skill=installed/'skills/gcpro-accounting' if (installed/'plugin.json').exists() else installed
  verify_manifest(skill)
  assert (skill/'SKILL.md').read_text(encoding='utf-8').splitlines()[1]=='name: gcpro-accounting'
  assert not (installed/'skills/gcpro-gas-report').exists()
  subprocess.run(['node',str(skill/'scripts/run-accounting.mjs'),'--verify-distribution'],capture_output=True,check=True)
  # Run a sanitized Inventory command from the installed ZIP, not source paths.
  inputs=Path(tmp)/'synthetic.csv';inputs.write_text('Date,Service Item,Job Code 1,Job Code 2,Hours\n2026-10-05,Contents,Synthetic customer,26-0001-CON,1\n',encoding='utf-8')
  response=subprocess.run(['node',str(skill/'scripts/run-accounting.mjs'),'--workflow','inventory','--timesheet',str(inputs),'--month','2026-10','--total','1.00','--output',str(Path(tmp)/'report')],capture_output=True,text=True,check=True)
  result=json.loads(response.stdout);assert result['verification']['success'] and result['pools'][0]['allocated']=='1.00'
 digest=sha(target.read_bytes());(DIST/(name+'.sha256')).write_text(digest+'  '+name+'\n',encoding='ascii')
 return {'file':str(target),'files':len(files),'bytes':target.stat().st_size,'sha256':digest,'installedSmokeTest':'PASS'}
results=[build(SKILL,'gcpro-accounting.zip','gcpro-accounting/'),build(PLUGIN,'gcpro-accounting-plugin.zip','')]
(DIST/'verification.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8');print(json.dumps(results,indent=2))
