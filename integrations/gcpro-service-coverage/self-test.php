<?php
namespace GCPRO\Coverage;

/** Synthetic fixtures only; no reads/writes to the operational register. */
final class SelfTest {
    public static function run() {
        $base=['kind'=>'city','value'=>'Example City','cities'=>['Example City'],'state'=>'IL','status'=>'served','aliases'=>['Example Alias'],'ambiguous'=>false,'partial'=>false,'geo_page_id'=>0,'approved'=>true,'archived'=>false,'note'=>'PRIVATE_FIXTURE_DO_NOT_EXPOSE'];
        $zip=array_merge($base,['kind'=>'zip','value'=>'00123']);
        $tests=[];
        $assert=static function($name,$actual,$expected)use(&$tests){$tests[$name]=$actual===$expected;};
        $status=static function($v,$rows,$enabled=true){return Engine::lookup($v,$rows,$enabled)['status'];};
        $assert('city_case_whitespace',$status('  eXamPle   CiTy ',[$base]),'served');
        $assert('reviewed_alias',$status('example alias',[$base]),'served');
        $assert('zip_leading_zero',$status('00123',[$zip]),'served');
        $assert('zip_plus_four',$status('00123-4567',[$zip]),'served');
        $assert('numeric_input_rejected',$status(123,[$zip]),'invalid');
        $assert('html_input_rejected',$status('<script>',[$zip]),'invalid');
        $assert('array_input_rejected',$status([],[$zip]),'invalid');
        $assert('unknown_not_excluded',$status('Other City',[$base]),'unresolved');
        $assert('disabled_approval_gate',$status('00123',[$zip],false),'requires_call');
        $unapproved=array_merge($zip,['approved'=>false]);
        $assert('unapproved_cannot_confirm',$status('00123',[$unapproved]),'unresolved');
        $assert('unreviewed_alias_ignored',$status('example alias',[array_merge($base,['approved'=>false])]),'unresolved');
        $ambiguous=array_merge($zip,['ambiguous'=>true]);
        $assert('ambiguous_zip',$status('00123',[$ambiguous]),'unresolved');
        $assert('partial_city',$status('Example City',[array_merge($base,['partial'=>true])]),'unresolved');
        $excluded=array_merge($ambiguous,['status'=>'not_served']);
        $assert('zip_exception_overrides_city',$status('00123',[$base,$excluded]),'not_served');
        $assert('city_with_zip_exception',$status('Example City',[$base,$excluded]),'requires_call');
        $assert('ambiguous_alias',$status('Example Alias',[$base,array_merge($base,['value'=>'Second City'])]),'unresolved');
        $assert('call_status',$status('Example City',[array_merge($base,['status'=>'requires_call'])]),'requires_call');
        $assert('unresolved_status',$status('Example City',[array_merge($base,['status'=>'unresolved'])]),'unresolved');
        $assert('archived_excluded',$status('Example City',[array_merge($base,['archived'=>true])]),'unresolved');
        $assert('private_note_excluded',strpos(json_encode(Engine::lookup('00123',[$zip],true)),'PRIVATE_FIXTURE')===false,true);
        $raw=['kind'=>'zip','value'=>'00123','cities'=>'Example City','state'=>'IL','status'=>'served','aliases'=>'Example Alias','ambiguous'=>'0','partial'=>'0','geo_page_id'=>'0','source'=>'Synthetic fixture','source_date'=>'2026-10-29','note'=>'=PRIVATE_FIXTURE'];
        $clean=Plugin::clean($raw);
        $assert('text_zip_retained',$clean['value'],'00123');
        $assert('clean_cannot_import_approval',Plugin::clean($raw+['approved'=>true])['approved'],false);
        $assert('invalid_zip_row',Plugin::clean(array_merge($raw,['value'=>'1234'])),null);
        $assert('invalid_date_row',Plugin::clean(array_merge($raw,['source_date'=>'2026-02-30'])),null);
        $assert('invalid_status_row',Plugin::clean(array_merge($raw,['status'=>'confirmed'])),null);
        $f=fopen('php://temp','r+');fputcsv($f,Plugin::COLUMNS,',','"','');
        $values=array_map(static function($k)use($raw){return Plugin::csv_cell($raw[$k]);},Plugin::COLUMNS);
        fputcsv($f,$values,',','"','');fputcsv($f,$values,',','"','');fputcsv($f,['bad'],',','"','');rewind($f);
        $out=Plugin::csv_import($f,[]);fclose($f);
        $assert('csv_duplicate_and_invalid_rows',[$out['added'],$out['skipped']],[1,2]);
        $saved=array_values($out['records'])[0];
        $assert('csv_text_round_trip',$saved['value'],'00123');
        $assert('csv_formula_guard_round_trip',$saved['note'],'=PRIVATE_FIXTURE');
        $assert('csv_stays_unapproved',$saved['approved'],false);
        $public=Plugin::response(Engine::lookup('00123',[$zip],true),0);
        $assert('public_fields_allowlisted',array_keys($public),['status','message','actions']);
        $assert('private_response_excluded',strpos(json_encode($public),'PRIVATE_FIXTURE')===false,true);
        $assert('not_served_no_enquiry',Plugin::response(['status'=>'not_served'],0)['actions'],[]);
        $assert('call_destination',Plugin::response(['status'=>'requires_call'],0)['actions'][0]['url'],'tel:+18476563322');
        return ['fixture_mode'=>'synthetic_in_memory_only','passed'=>count(array_filter($tests)),'total'=>count($tests),'checks'=>$tests];
    }
}
