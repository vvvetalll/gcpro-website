<?php
/**
 * Plugin Name: GCPRO Service Coverage
 * Description: Reviewed city/ZIP register and lookup for the existing Elementor availability popup.
 * Version: 1.2.2
 * Requires PHP: 7.4
 * License: GPL-2.0-or-later
 */
namespace GCPRO\Coverage;
if (!defined('ABSPATH')) exit;
require_once __DIR__.'/engine.php';

final class Plugin {
    const OPTION = 'gcpro_service_coverage_v1';
    const PAGE = 'gcpro-service-coverage';
    const VERSION = '1.2.2';
    const COLUMNS = ['kind','value','cities','state','status','aliases','ambiguous','partial','geo_page_id','source','source_date','note'];
    public static function init() {
        add_action('admin_menu', [__CLASS__, 'menu']);
        add_action('admin_enqueue_scripts', static function($hook){if($hook==='toplevel_page_'.self::PAGE) wp_enqueue_style('gcpro-coverage-admin',plugins_url('admin.css',__FILE__),[],self::VERSION);});
        foreach (['save','settings','import','export','archive'] as $action) add_action('admin_post_gcpro_coverage_'.$action, [__CLASS__, $action]);
        add_action('rest_api_init', static function() {
            register_rest_route('gcpro-coverage/v1', '/lookup', ['methods'=>'POST','permission_callback'=>'__return_true','callback'=>[__CLASS__,'lookup']]);
            register_rest_route('gcpro-coverage/v1', '/register', ['methods'=>'GET','permission_callback'=>static function(){return current_user_can('manage_options');},'callback'=>static function(){ $r=new \WP_REST_Response(self::db());$r->header('Cache-Control','no-store');return $r; }]);
            register_rest_route('gcpro-coverage/v1', '/record', ['methods'=>'POST','permission_callback'=>static function(){return current_user_can('manage_options');},'callback'=>[__CLASS__,'api_save']]);
            register_rest_route('gcpro-coverage/v1', '/self-test', ['methods'=>'POST','permission_callback'=>static function(){ return current_user_can('manage_options'); },'callback'=>static function(){ require_once __DIR__.'/self-test.php'; return new \WP_REST_Response(SelfTest::run()); }]);
        });
        add_filter('elementor/widget/render_content', [__CLASS__, 'popup_content'], 20, 2);
    }
    public static function activate() {
        if (get_option(self::OPTION, null) !== null) return;
        $seed = json_decode(file_get_contents(__DIR__.'/proposal-seed.json'), true);
        $rows = [];
        foreach ((array)$seed as $raw) { $r = self::clean($raw); if ($r) $rows[self::key($r)] = $r; }
        add_option(self::OPTION, ['revision'=>1,'enabled'=>false,'bridge'=>false,'request_page'=>492,'records'=>$rows], '', false);
    }
    public static function db() { $d = get_option(self::OPTION, []); return is_array($d) ? $d : []; }
    public static function key($r) { return $r['kind'].':'.Engine::normalize($r['value']).':'.$r['state']; }
    public static function clean($raw) {
        foreach (self::COLUMNS as $k) if (isset($raw[$k]) && !is_scalar($raw[$k]) && !in_array($k,['cities','aliases'],true)) return null;
        $kind = $raw['kind'] ?? ''; $value = trim((string)($raw['value'] ?? ''));
        if (!in_array($kind,['city','zip'],true)) return null;
        $input = Engine::input($value);
        if (!$input || $input[0] !== $kind || ($kind==='zip' && !preg_match('/^[0-9]{5}$/D',$value))) return null;
        $state = strtoupper(trim((string)($raw['state'] ?? '')));
        $status = $raw['status'] ?? '';
        if (!preg_match('/^[A-Z]{2}$/D',$state) || !in_array($status,['served','requires_call','not_served','unresolved'],true)) return null;
        $list = static function($x) { return array_values(array_unique(array_filter(array_map('sanitize_text_field', is_array($x) ? $x : explode('|',(string)$x))))); };
        $cities = $list($raw['cities'] ?? ''); $aliases = $list($raw['aliases'] ?? '');
        foreach (array_merge($cities,$aliases) as $city) { $i=Engine::input($city); if (!$i || $i[0]!=='city') return null; }
        if (!$cities) return null;
        $page = (string)($raw['geo_page_id'] ?? '0'); if ($page==='') $page='0';
        if (!preg_match('/^[0-9]+$/D',$page)) return null;
        if ((int)$page && get_post_type((int)$page) !== 'page') return null;
        $date = (string)($raw['source_date'] ?? '');
        if ($date !== '' && (!preg_match('/^\d{4}-\d{2}-\d{2}$/D',$date) || !checkdate((int)substr($date,5,2),(int)substr($date,8,2),(int)substr($date,0,4)))) return null;
        return ['kind'=>$kind,'value'=>$value,'cities'=>$cities,'state'=>$state,'status'=>$status,'aliases'=>$aliases,
            'ambiguous'=>in_array($raw['ambiguous'] ?? false,[true,1,'1'],true),'partial'=>in_array($raw['partial'] ?? false,[true,1,'1'],true),
            'geo_page_id'=>(int)$page,'source'=>sanitize_text_field($raw['source'] ?? ''),'source_date'=>$date,'note'=>sanitize_textarea_field($raw['note'] ?? ''),
            'approved'=>false,'approval_reference'=>'','approved_by'=>0,'approved_at'=>'','archived'=>false];
    }
    private static function guard($action) {
        if (!current_user_can('manage_options')) wp_die('Access denied', '', ['response'=>403]);
        check_admin_referer('gcpro_coverage_'.$action);
        if ($action !== 'export' && (int)($_POST['revision'] ?? -1) !== (int)(self::db()['revision'] ?? 0)) wp_die('The register changed. Reload before saving.', '', ['response'=>409]);
    }
    private static function persist(&$d) { $d['revision']++; update_option(self::OPTION,$d,false); }
    private static function done($message) { wp_safe_redirect(add_query_arg(['page'=>self::PAGE,'notice'=>$message],admin_url('admin.php'))); exit; }
    private static function form($action,$multipart=false) {
        echo '<form method="post" action="'.esc_url(admin_url('admin-post.php')).'"'.($multipart?' enctype="multipart/form-data"':'').'>';
        wp_nonce_field('gcpro_coverage_'.$action);
        echo '<input type="hidden" name="action" value="gcpro_coverage_'.esc_attr($action).'"><input type="hidden" name="revision" value="'.esc_attr(self::db()['revision'] ?? 0).'">';
    }
    public static function menu() { add_menu_page('GCPRO Coverage','GCPRO Coverage','manage_options',self::PAGE,[__CLASS__,'admin'],'dashicons-location-alt',81); }
    private static function query($key) { return isset($_GET[$key]) && is_string($_GET[$key]) ? sanitize_text_field(wp_unslash($_GET[$key])) : ''; }
    private static function url($args=[]) { return add_query_arg(array_merge(['page'=>self::PAGE],$args),admin_url('admin.php')); }
    public static function admin() {
        if (!current_user_can('manage_options')) return;
        $d=self::db(); $rows=$d['records']; ksort($rows,SORT_STRING);
        $key=self::query('edit'); $view=$key?'edit':self::query('view');
        if (!in_array($view,['edit','settings','import'],true)) $view='register';
        $r=$rows[$key]??['kind'=>'city','state'=>'IL','status'=>'requires_call','geo_page_id'=>0];
        $approved=count(array_filter($rows,static function($x){return !empty($x['approved'])&&empty($x['archived']);}));
        echo '<div class="wrap gcpro-coverage-admin"><header class="gcpro-admin-header"><div><p class="gcpro-eyebrow">GCPRO / OPERATIONS</p><h1>Service coverage</h1><p>Review geographic records before enabling customer-facing decisions.</p></div><a class="button button-primary" href="'.esc_url(self::url(['view'=>'edit'])).'">Add location</a></header>';
        echo '<div class="gcpro-summary"><div><strong>'.count($rows).'</strong><span>City &amp; ZIP records</span></div><div><strong>'.$approved.'</strong><span>Approved records</span></div><div><strong>'.(count($rows)-$approved).'</strong><span>Pending review / archived</span></div><div><span class="gcpro-badge '.(!empty($d['enabled'])?'is-approved':'is-pending').'">'.(!empty($d['enabled'])?'Matching enabled':'Confirmation disabled').'</span><span>'.(!empty($d['bridge'])?'Elementor popup connected':'Popup connection pending').'</span></div></div>';
        echo '<nav class="gcpro-admin-tabs" aria-label="Coverage management">';
        foreach(['register'=>'Coverage register','edit'=>'Add / edit location','settings'=>'Popup & approval','import'=>'Import / export'] as $v=>$label) echo '<a '.($view===$v?'aria-current="page"':'').' href="'.esc_url(self::url(['view'=>$v])).'">'.esc_html($label).'</a>';
        echo '</nav>';
        $notice=self::query('notice'); $notices=['saved'=>'Location saved. Any approval applies only to that individual record.','settings'=>'Settings saved.','archived'=>'Record archived and retained for recovery.','invalid'=>'Check the ZIP/city, state, status, source date and page object.','approval'=>'Approval needs its typed confirmation and owner decision reference. Ambiguous or partial records cannot be approved as served.','file'=>'CSV rejected: unreadable, over limit, or invalid header.'];
        if(isset($notices[$notice])) echo '<div class="notice notice-info inline"><p>'.esc_html($notices[$notice]).'</p></div>';
        if($notice==='import') echo '<div class="notice notice-info inline"><p>'.esc_html(sprintf('Imported %d unapproved records; skipped %d invalid, duplicate or already-approved rows. No approvals imported.',absint($_GET['added']??0),absint($_GET['skipped']??0))).'</p></div>';
        if($view==='register') {
            $search=self::query('search');$status=self::query('status');$kind=self::query('kind');
            $filtered=array_filter($rows,static function($x)use($search,$status,$kind){return (!$search||stripos($x['value'].' '.implode(' ',$x['cities']),$search)!==false)&&(!$status||$x['status']===$status)&&(!$kind||$x['kind']===$kind);});
            echo '<section class="gcpro-admin-panel"><div class="gcpro-panel-title"><h2>Coverage register</h2><p>Proposed coverage is not approved service eligibility. Unknown input stays unconfirmed.</p></div><form method="get" class="gcpro-register-search"><input type="hidden" name="page" value="'.esc_attr(self::PAGE).'"><label><span class="screen-reader-text">Find city or ZIP</span><input name="search" value="'.esc_attr($search).'" placeholder="Find a city or ZIP…" type="search"></label><label><span class="screen-reader-text">Record type</span><select name="kind"><option value="">All record types</option>';foreach(['city'=>'Cities','zip'=>'ZIP codes']as$v=>$label)echo '<option value="'.esc_attr($v).'" '.selected($kind,$v,false).'>'.esc_html($label).'</option>';echo '</select></label><label><span class="screen-reader-text">Coverage status</span><select name="status"><option value="">All coverage statuses</option>';foreach(['served'=>'Served proposal','requires_call'=>'Requires a call','not_served'=>'Not served','unresolved'=>'Unresolved']as$v=>$label)echo '<option value="'.esc_attr($v).'" '.selected($status,$v,false).'>'.esc_html($label).'</option>';echo '</select></label><button class="button" type="submit">Filter records</button><a href="'.esc_url(self::url()).'">Reset</a></form>';
            $count=count($filtered);$page=max(1,min(max(1,(int)ceil($count/25)),absint(self::query('paged'))?:1));$visible=array_slice($filtered,($page-1)*25,25,true);
            echo '<div class="gcpro-table-scroll"><table class="widefat"><thead><tr><th>Location</th><th>Geographic association</th><th>Coverage</th><th>Review</th><th>Geo page</th><th><span class="screen-reader-text">Edit</span></th></tr></thead><tbody>';
            foreach($visible as $k=>$x) {
                $city=implode(', ',array_slice($x['cities'],0,3));if(count($x['cities'])>3)$city.=' +'.(count($x['cities'])-3).' more';
                $labels=['served'=>'Served proposal','requires_call'=>'Requires a call','not_served'=>'Not served','unresolved'=>'Unresolved'];
                echo '<tr><td><a class="gcpro-record-name" href="'.esc_url(self::url(['edit'=>$k])).'">'.esc_html($x['value']).'</a><small>'.esc_html(($x['kind']==='zip'?'ZIP code':'City').' · '.$x['state']).'</small></td><td><span title="'.esc_attr(implode(', ',$x['cities'])).'">'.esc_html($city).'</span><small>'.esc_html(($x['ambiguous']?'Cross-boundary / ambiguous · ':'').($x['partial']?'Partial area · ':'').$x['source_date']).'</small></td><td>'.esc_html($x['approved']&&$x['status']==='served'?'Served':$labels[$x['status']]).'</td><td><span class="gcpro-badge '.($x['approved']?'is-approved':'is-pending').'">'.esc_html($x['archived']?'Archived':($x['approved']?'Approved':'Proposed')).'</span></td><td>';
                if($x['geo_page_id'])echo '<a href="'.esc_url(get_edit_post_link($x['geo_page_id'])).'">'.esc_html(get_the_title($x['geo_page_id'])).'</a><small>'.esc_html(get_post_status($x['geo_page_id'])).'</small>';else echo '<span class="gcpro-muted">—</span>';
                echo '</td><td><a class="button button-small" href="'.esc_url(self::url(['edit'=>$k])).'">Edit</a></td></tr>';
            }
            if(!$count)echo '<tr><td colspan="6">No records match these filters. <a href="'.esc_url(self::url()).'">Reset filters</a></td></tr>';
            echo '</tbody></table></div><div class="gcpro-table-bottom"><span>'.esc_html($count.' matching records · page '.$page.' of '.max(1,(int)ceil($count/25))).'</span><div>'.wp_kses_post(paginate_links(['base'=>add_query_arg('paged','%#%',self::url(['search'=>$search,'status'=>$status,'kind'=>$kind])),'format'=>'','current'=>$page,'total'=>max(1,(int)ceil($count/25)),'prev_text'=>'← Previous','next_text'=>'Next →'])).'</div></div></section>';
        } elseif($view==='edit') {
            echo '<section class="gcpro-admin-panel gcpro-editor"><div class="gcpro-panel-title"><h2>'.($key?'Edit location':'Add location').'</h2><p>ZIPs stay five-character text. Separate associated cities and reviewed aliases with |.</p></div>'; self::form('save');echo '<input type="hidden" name="original_key" value="'.esc_attr($key).'"><div class="gcpro-field-grid">';
            $labels=['kind'=>'Record type','value'=>'City name or ZIP','cities'=>'Associated city / cities','state'=>'State','status'=>'Proposed coverage status','aliases'=>'Reviewed city aliases','ambiguous'=>'Geographic ambiguity','partial'=>'Partial city coverage','geo_page_id'=>'Optional WordPress geo page ID','source'=>'Geographic / decision source','source_date'=>'Source review date','note'=>'Private administrative note'];
            foreach(self::COLUMNS as $col) {
                $value=$r[$col]??'';if(is_array($value))$value=implode('|',$value);if(is_bool($value))$value=$value?'1':'0';
                echo '<label class="gcpro-field '.(in_array($col,['source','note','cities'],true)?'is-wide':'').'"><span>'.esc_html($labels[$col]).'</span>';
                if(in_array($col,['kind','status','ambiguous','partial'],true)) {
                    $options=$col==='kind'?['city'=>'City','zip'=>'ZIP code']:($col==='status'?['served'=>'Served — proposal until approved','requires_call'=>'Requires a call','not_served'=>'Not served','unresolved'=>'Unresolved']:['0'=>'No','1'=>'Yes']);echo '<select name="'.esc_attr($col).'">';foreach($options as$v=>$label)echo '<option value="'.esc_attr($v).'" '.selected((string)$value,(string)$v,false).'>'.esc_html($label).'</option>';echo '</select>';
                } elseif($col==='note')echo '<textarea rows="3" name="note">'.esc_textarea($value).'</textarea><small>Admin only. Never returned by the public checker. CSV exports contain this note and must stay private.</small>';
                else echo '<input name="'.esc_attr($col).'" value="'.esc_attr($value).'" '.($col==='source_date'?'type="date"':'type="text"').' '.(in_array($col,['value','cities','state','source','source_date'],true)?'required':'').'>';
                echo '</label>';
            }
            echo '</div><fieldset class="gcpro-approval-box"><legend>Individual owner approval</legend><p>Saving edits resets the previous approval. Import cannot approve records. Ambiguous or partial records cannot confirm service.</p><label><input type="checkbox" name="approve" value="1"> Approve this specific record</label><div class="gcpro-field-grid"><label class="gcpro-field"><span>Owner decision reference</span><input name="approval_reference" value="'.esc_attr($r['approval_reference']??'').'"></label><label class="gcpro-field"><span>Type APPROVE to confirm</span><input name="approve_confirm" autocomplete="off"></label></div></fieldset><div class="gcpro-editor-actions">';submit_button('Save location','primary','submit',false);echo '<a class="button" href="'.esc_url(self::url()).'">Back to register</a></div></form>';
            if($key){echo '<details class="gcpro-archive"><summary>Archive this record</summary><p>Retains the record for recovery and removes it from matching.</p>';self::form('archive');echo '<input type="hidden" name="key" value="'.esc_attr($key).'"><label>Type ARCHIVE <input name="confirm" required></label>';submit_button('Archive one record','secondary');echo '</form></details>';}
            echo '</section>';
        } elseif($view==='settings') {
            echo '<section class="gcpro-admin-panel gcpro-editor"><div class="gcpro-panel-title"><h2>Popup connection &amp; approval</h2><p>Elementor retains the modal and native form. No second popup or trigger is created.</p></div>';self::form('settings');
            echo '<div class="gcpro-setting-row"><label><input type="checkbox" name="bridge" value="1" '.checked(!empty($d['bridge']),true,false).'> Connect this register to Elementor Popup1801</label><p>This replaces the old popup-local matcher at render time. It does not enable proposed coverage decisions.</p></div><div class="gcpro-setting-row"><label>Request Service WordPress page ID <input name="request_page" type="number" min="1" value="'.esc_attr($d['request_page']).'"></label><p>Native object reference; the current Published permalink is resolved when a result is shown.</p></div><fieldset class="gcpro-approval-box"><legend>Operational decision gate</legend><label><input type="checkbox" name="enabled" value="1" '.checked(!empty($d['enabled']),true,false).'> Enable approved operational decisions</label><p>Leave disabled until the owner approves the coverage register. Individual records also require approval.</p><div class="gcpro-field-grid"><label class="gcpro-field"><span>Owner approval reference</span><input name="gate_reference" value="'.esc_attr($d['gate_reference']??'').'"></label><label class="gcpro-field"><span>Type ENABLE to activate</span><input name="enable_confirm" autocomplete="off"></label></div></fieldset>';
            submit_button('Save settings');echo '</form></section>';
        } else {
            echo '<div class="gcpro-import-grid"><section class="gcpro-admin-panel"><div class="gcpro-panel-title"><h2>Import records</h2><p>Merge reviewed geographic data as unapproved proposals.</p></div><ul><li>No bulk approval or deletion.</li><li>Already-approved records are skipped.</li><li>First valid duplicate wins; later duplicates are skipped.</li><li>Maximum5000 rows /2MB. Invalid imports do not partially save on a fatal file error.</li></ul>';self::form('import',true);echo '<label class="gcpro-field"><span>Coverage CSV file</span><input name="csv" type="file" accept=".csv,text/csv" required></label>';submit_button('Import unapproved CSV');echo '</form><details><summary>Required CSV columns</summary><p><code>'.esc_html(implode(',',self::COLUMNS)).'</code></p></details></section><section class="gcpro-admin-panel"><div class="gcpro-panel-title"><h2>Export &amp; recovery</h2><p>Download the current authoritative register.</p></div><p>Includes source references, approval indicators and private administrative notes. Keep exports private. Re-import never approves records.</p>';self::form('export');submit_button('Export private CSV','secondary');echo '</form></section></div>';
        }
        echo '<p class="gcpro-admin-footnote">GCPRO Service Coverage · Database register only · Geographic association ≠ business approval · No visitor search tracking</p></div>';
    }
    public static function save_one($raw,$revision) {
        $d=self::db();
        if ((int)$revision !== (int)$d['revision']) return new \WP_Error('coverage_conflict','Reload the current register before editing.',['status'=>409]);
        if (!is_array($raw)) return new \WP_Error('invalid','Invalid record.',['status'=>400]);
        $r=self::clean($raw);
        if(!$r || !$r['source'] || !$r['source_date']) return new \WP_Error('invalid','Invalid record.',['status'=>400]);
        if (!empty($raw['approve'])) {
            $ref=sanitize_text_field($raw['approval_reference']??'');
            if (($raw['approve_confirm']??'')!=='APPROVE' || !$ref || ($r['status']==='served' && ($r['ambiguous']||$r['partial']))) return new \WP_Error('approval','Individual typed approval and source required.',['status'=>400]);
            $r['approved']=true;$r['approval_reference']=$ref;$r['approved_by']=get_current_user_id();$r['approved_at']=gmdate('c');
        }
        $key=self::key($r);$old=$raw['original_key']??'';
        if ($old && $old!==$key) return new \WP_Error('invalid','Identity is stable. Add a new record and archive the old one.',['status'=>400]);
        $d['records'][$key]=$r;self::persist($d);return ['saved'=>true,'key'=>$key,'revision'=>$d['revision'],'approved'=>$r['approved']];
    }
    public static function api_save($request) {
        $body=$request->get_json_params();if(!is_array($body)) return new \WP_Error('invalid','JSON record required.',['status'=>400]);
        return self::save_one($body['record']??null,$body['revision']??-1);
    }
    public static function save() {
        self::guard('save');$raw=wp_unslash($_POST);$result=self::save_one($raw,$raw['revision']??-1);
        self::done(is_wp_error($result)?$result->get_error_code():'saved');
    }
    public static function settings() {
        self::guard('settings'); $d=self::db(); $raw=wp_unslash($_POST); $enable=!empty($raw['enabled']);
        $ref=sanitize_text_field($raw['gate_reference']??'');
        if ($enable && (($raw['enable_confirm']??'')!=='ENABLE' || !$ref)) self::done('approval');
        $id=absint($raw['request_page']??0); if (!$id || get_post_type($id)!=='page') self::done('invalid');
        $d['enabled']=$enable; $d['bridge']=!empty($raw['bridge']); $d['gate_reference']=$ref; $d['request_page']=$id; self::persist($d); self::done('settings');
    }
    public static function archive() {
        self::guard('archive'); $key=sanitize_text_field(wp_unslash($_POST['key']??'')); $d=self::db();
        if (($_POST['confirm']??'')!=='ARCHIVE' || !isset($d['records'][$key])) self::done('invalid');
        $d['records'][$key]['archived']=true; $d['records'][$key]['approved']=false; self::persist($d); self::done('archived');
    }
    public static function csv_import($f, array $existing) {
        $header=fgetcsv($f,0,',','"','');
        if (!$header) return null;
        $header=array_map(static function($x){ return trim(preg_replace('/^\xEF\xBB\xBF/','',$x)); },$header);
        if (array_diff(self::COLUMNS,$header) || count($header)!==count(array_unique($header))) return null;
        $added=0; $skipped=0; $seen=[]; $line=0;
        while (($values=fgetcsv($f,0,',','"',''))!==false) {
            if (++$line>5000) return null;
            if (count($values)!==count($header)) { $skipped++; continue; }
            $values=array_map(static function($x){ return preg_replace('/^\'(?=\s*[=+@\-])/','',$x); },$values);
            $r=self::clean(array_combine($header,$values));
            if (!$r || !$r['source'] || !$r['source_date']) { $skipped++; continue; }
            $key=self::key($r);
            if (isset($seen[$key]) || !empty($existing[$key]['approved'])) { $skipped++; continue; }
            $seen[$key]=true; $existing[$key]=$r; $added++;
        }
        return ['records'=>$existing,'added'=>$added,'skipped'=>$skipped];
    }
    public static function import() {
        self::guard('import'); $file=$_FILES['csv']??[];
        if (empty($file['tmp_name']) || !is_uploaded_file($file['tmp_name']) || ($file['error']??1)!==UPLOAD_ERR_OK || $file['size']>2097152) self::done('file');
        $f=fopen($file['tmp_name'],'r'); if(!$f) self::done('file'); $d=self::db(); $out=self::csv_import($f,$d['records']); fclose($f); if(!$out) self::done('file');
        $d['records']=$out['records']; self::persist($d);
        wp_safe_redirect(add_query_arg(['page'=>self::PAGE,'notice'=>'import','added'=>$out['added'],'skipped'=>$out['skipped']],admin_url('admin.php'))); exit;
    }
    public static function csv_cell($v) { if(is_array($v)) $v=implode('|',$v); if(is_bool($v)) $v=$v?'1':'0'; $v=(string)$v; return preg_match('/^\s*[=+@\-]/',$v)?"'".$v:$v; }
    public static function export() {
        self::guard('export'); nocache_headers(); header('Content-Type: text/csv; charset=utf-8'); header('Content-Disposition: attachment; filename="gcpro-coverage-private.csv"');
        $out=fopen('php://output','w'); $cols=array_merge(self::COLUMNS,['approved','approval_reference','approved_by','approved_at','archived']); fputcsv($out,$cols,',','"','');
        foreach(self::db()['records'] as $r) fputcsv($out,array_map(static function($k)use($r){return self::csv_cell($r[$k]??'');},$cols),',','"',''); fclose($out); exit;
    }
    public static function response($match, $request_page) {
        $s=$match['status']; $actions=[];
        $messages=['invalid'=>'Enter a city name or a five-digit ZIP code.','requires_call'=>'Please call to confirm service at your address.','unresolved'=>'We couldn’t confirm coverage for this location. Please call us.','not_served'=>'We don’t currently provide service at this location.','served'=>'We serve this area.'];
        $message=$messages[$s]??$messages['unresolved'];
        if ($s==='served') {
            $geo=$match['geo_page_id']??0; $city=$match['city']??'';
            if ($city && $geo && get_post_status($geo)==='publish' && get_post_type($geo)==='page') {
                $message='We serve '.$city.', '.$match['state'].'.'; $actions[]=['label'=>'View services in '.$city,'url'=>get_permalink($geo)];
            }
            if (get_post_status($request_page)==='publish' && get_post_type($request_page)==='page') $actions[]=['label'=>'Request Service','url'=>get_permalink($request_page)];
        } elseif (in_array($s,['requires_call','unresolved'],true)) $actions[]=['label'=>'Call Now','url'=>'tel:+18476563322'];
        return ['status'=>$s,'message'=>$message,'actions'=>$actions];
    }
    public static function lookup($request) {
        $body=$request->get_json_params(); $value=is_array($body)?($body['location']??null):null; $d=self::db();
        $match=Engine::lookup($value,$d['records']??[],!empty($d['enabled']));
        $r=new \WP_REST_Response(self::response($match,$d['request_page']??0),$match['status']==='invalid'?400:200);
        $r->header('Cache-Control','no-store, max-age=0'); return $r;
    }
    public static function popup_content($content,$widget) {
        $d=self::db(); if(empty($d['bridge']) || $widget->get_id()!=='7a5e1801') return $content;
        // Existing HTML widget7a5e1801 belongs only to Popup1801. Widget_Base has no get_document() API.
        if ($widget->get_name() !== 'html') return $content;
        // Native Elementor owns modal/form geometry; this stylesheet owns only dynamic results.
        return '<link rel="stylesheet" href="'.esc_url(plugins_url('popup.css',__FILE__)).'?ver='.self::VERSION.'"><div data-gcpro-availability data-endpoint="'.esc_url(rest_url('gcpro-coverage/v1/lookup')).'"><p id="gcpro-coverage-error" data-error role="alert"></p><p data-result role="status" aria-live="polite" aria-atomic="true"></p><div data-coverage-actions></div><p class="coverage-note">Geographic coverage only.</p></div><script src="'.esc_url(plugins_url('popup.js',__FILE__)).'?ver='.self::VERSION.'"></script>';
    }
}
register_activation_hook(__FILE__,[Plugin::class,'activate']);
Plugin::init();
