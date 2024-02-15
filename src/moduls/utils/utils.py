import os, json, importlib, sys

def send_postdata(file_id, postdata):
    dir_principal = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
    route = os.path.join(dir_principal, 'moduls', 'postdata', f'{file_id}.py')
    data = f'content = {postdata}'
    open(route, "w").write(data)

def get_postdata(file_id):
    try:
        module_name = f"moduls.postdata.start"
        module = importlib.import_module(module_name)
        variable = module.content
        
        # Eliminar el archivo start.py
        module_path = module.__file__
        if os.path.exists(module_path):
            os.remove(module_path)
        
        # Eliminar el módulo importado
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        return variable
    except ModuleNotFoundError:
        return None
    
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

def load_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dir_principal = os.path.abspath(os.path.join(current_dir, '..', '..'))
    route = os.path.join(dir_principal, 'config', 'config.json')
    with open(route) as archivo_config:
        config = json.load(archivo_config)    
    return config

def save_api_key(api_key):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")
    with open(config_path, "w") as config_file:
        json.dump({"api_key": api_key}, config_file)    

if __name__ == "__main__":
    print ("Utilities system")