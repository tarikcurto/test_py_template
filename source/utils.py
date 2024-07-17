import json
import re

from source.adhoc_funcs import adhoc_funcs
from source.transform_funcs import tranform_funcs

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def parse_and_replace(json_content, local_vars, global_vars, entorno):
    pattern = re.compile(r'{{vars/(\w+) ?\|? ?([\w\ |]+)?}}')

    def get_value(var_name, vars_dict):
        var_info = vars_dict.get(var_name, {})
        var_type = var_info.get("type")
        var_value = var_info.get("value")
        
        if not var_value:
            return None

        if var_type == "unique":
            return var_value
        elif var_type == "env":
            return var_value.get(entorno)
        elif var_type == "adhoc":
            if var_name in adhoc_funcs:
                return adhoc_funcs[var_name](var_value)
            else:
                print(f"missing adhoc function {var_name}")
                return None
        else:
            print(f"var type {var_type} not implemented")
            return None

    def replacer(match):
        var_name = match.group(1)
        transformers = match.group(2)

        result = get_value(var_name, local_vars) or get_value(var_name, global_vars)
        if result is None:
            print(f"failed to resolve var {var_name}")
            result = match.group(0)
        
        if not transformers or len(transformers) == 0:
            return result
    
        transformers = [_.strip() for _ in transformers.split('|')]
        for transformer in transformers:
            if transformer in tranform_funcs:
                result = tranform_funcs[transformer](result)
            else:
                print(f"missing transformer {transformer}")
            
        return result

    json_str = json.dumps(json_content)
    replaced_str = pattern.sub(replacer, json_str)
    return json.loads(replaced_str)
