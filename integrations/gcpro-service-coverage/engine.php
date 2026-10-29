<?php
namespace GCPRO\Coverage;

/** Pure matching rules. No storage, WordPress globals, tracking or network. */
final class Engine {
    public static function normalize($value) {
        return strtolower(trim(preg_replace('/\s+/u', ' ', (string) $value)));
    }
    public static function input($value) {
        if (!is_string($value) || strlen($value) > 100) return null;
        $value = self::normalize($value);
        if (preg_match('/^([0-9]{5})(?:-[0-9]{4})?$/D', $value, $m)) return ['zip', $m[1]];
        if (strlen($value) <= 80 && preg_match("/^[a-z]+(?:[ .’'\-]+[a-z]+)*$/uD", $value)) return ['city', $value];
        return null;
    }
    public static function lookup($value, array $records, $enabled) {
        $input = self::input($value);
        if (!$input) return ['status'=>'invalid'];
        list($kind, $key) = $input;
        $matches = array_values(array_filter($records, static function($r) use ($kind, $key) {
            if (!empty($r['archived']) || $r['kind'] !== $kind) return false;
            $names = [$r['value']];
            // Aliases are operational only after the individual record is reviewed.
            if (!empty($r['approved'])) $names = array_merge($names, $r['aliases']);
            return in_array($key, array_map([__CLASS__, 'normalize'], $names), true);
        }));
        if (!$matches) return ['status'=>'unresolved'];
        if (!$enabled) return ['status'=>'requires_call'];
        if (count($matches) !== 1) return ['status'=>'unresolved'];
        $r = $matches[0];
        if (empty($r['approved'])) return ['status'=>'unresolved'];
        // An approved exact ZIP exclusion wins even when its geographic mapping is ambiguous.
        if ($kind === 'zip' && $r['status'] === 'not_served') return ['status'=>'not_served'];
        if (!empty($r['ambiguous']) || !empty($r['partial'])) return ['status'=>'unresolved'];
        if ($kind === 'city') {
            foreach ($records as $z) {
                if (!empty($z['archived']) || $z['kind'] !== 'zip' || empty($z['approved'])) continue;
                if (!in_array($z['status'], ['not_served','requires_call','unresolved'], true) && empty($z['partial']) && empty($z['ambiguous'])) continue;
                $city_names = array_map([__CLASS__, 'normalize'], array_merge([$r['value']], $r['aliases']));
                if (array_intersect($city_names, array_map([__CLASS__, 'normalize'], $z['cities']))) return ['status'=>'requires_call'];
            }
        }
        $out = ['status'=>$r['status']];
        if ($r['status'] === 'served') {
            $out['city'] = count($r['cities']) === 1 ? $r['cities'][0] : '';
            $out['state'] = $r['state'];
            $out['geo_page_id'] = $r['geo_page_id'];
        }
        return $out;
    }
}
