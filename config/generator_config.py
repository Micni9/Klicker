import json

def load_generator_cfg(generator_count):
    generator_cfg = {"price": [10**i for i in range(generator_count)]}
    return generator_cfg