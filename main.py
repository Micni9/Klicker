import sys
from utils import *
from config.config import load_cfg
from game_utils import *
import threading
import time

CFG_PATH = "./config/config.json"
TITLE = "KLICKER"

cfg, generator_cfg = load_cfg(CFG_PATH)

GM = GameManager(cfg, generator_cfg)
GM.game_start()

t = RepeatTimer(0.05,GM._game_tick)
t.start()
stop_event = threading.Event()
prompt = "Choose your action: Q to quit, 1-9 to buy generator, P to prestige, R to refresh:"
input_thread = threading.Thread(target=player_input,args=(prompt,t,GM,stop_event))
input_thread.daemon = True
input_thread.start()


try:
    while not stop_event.is_set():
        time.sleep(1)
except KeyboardInterrupt:
    stop_event.set()

t.cancel()

sys.exit()