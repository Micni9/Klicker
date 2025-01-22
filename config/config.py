import json
from .generator_config import load_generator_cfg

def load_cfg(fp):
    try:
        with open(fp,"r") as f:
            cfg = json.load(f)
    except Exception as e:
        print("Invalid json file")
        return None
    print(f"Config file is read.")
    generator_cfg = load_generator_cfg(cfg["generator_count"])
    return cfg, generator_cfg