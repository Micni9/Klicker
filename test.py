from config.config import load_cfg

from utils import *
from game_utils import *

cfg, generator_cfg = load_cfg("config/config.json")
GM = GameManager(cfg,generator_cfg)

GM.game_start()

GM.generator_list[8].add(1)

ticks = 2000
buy_count = 20
print(GM)
fast_forward(GM,ticks)
print(GM)
    
GM.generator_list[0].add(buy_count)
print(f"Buy {buy_count} generator 1.")
fast_forward(GM,ticks)
print(GM)
print(f"SCORE: {GM.score}")
GM.prestige()
print(GM)
fast_forward(GM,ticks)
print(GM)
