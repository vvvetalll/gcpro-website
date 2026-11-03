"""Compile the single Elementor Custom Code deployment artifact. No runtime dependencies."""
from pathlib import Path
import json
HERE=Path(__file__).parent
js=(HERE/'map.js').read_text(encoding='utf-8')
js=js.replace('/* MAP_PANEL */null',json.dumps((HERE/'map-panel.html').read_text(encoding='utf-8')))
js=js.replace('/* MAP_CSS */null',json.dumps((HERE/'map.css').read_text(encoding='utf-8')))
(HERE/'custom-code.html').write_text('<script>'+js+'</script>',encoding='utf-8')
