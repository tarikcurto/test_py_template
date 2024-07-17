import os
import sys
import tempfile
import json

from source.utils import load_json, parse_and_replace

def main():
    if len(sys.argv) != 5:
        print("Uso: script.py <ruta_vars_globales> <ruta_vars_locales> <entorno> <template>")
        sys.exit(1)

    ruta_vars_globales = sys.argv[1]
    ruta_vars_locales = sys.argv[2]
    entorno = sys.argv[3]
    template = sys.argv[4]

    global_vars = load_json(ruta_vars_globales)
    local_vars = load_json(ruta_vars_locales)
    target_json = load_json(template)

    processed_json = parse_and_replace(target_json, local_vars, global_vars, entorno)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.json', mode='w', encoding='utf-8') as temp_file:
        json.dump(processed_json, temp_file, ensure_ascii=False, indent=4)
        output_path = temp_file.name

    os.environ['PRE_PROCESSOR_OUTPUT_PATH'] = output_path
    print(f"Archivo procesado guardado en: {output_path}")

if __name__ == "__main__":
    main()
