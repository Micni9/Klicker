from utils import GameManager
from threading import Timer
import os

def fast_forward(GM:GameManager, ticks_passed):
    for _ in range(ticks_passed):
        GM._game_tick()
    print(f"Skipped {ticks_passed} ticks.")
    
def player_input(prompt,t,GM,stop_event):
    while not stop_event.is_set():
        action = input(prompt)
        if action == "Q" or action == "q":
            t.cancel()
            print("Game ended")
            print(GM.currency)
            stop_event.set()
            break
        if action.isdigit():
            choice = int(action)-1
            if choice >= 0 and choice < 9:
                GM.buy_generator(choice)
                print(GM)
            else:
                print(f"Fail to buy Generator {choice+1}")
        if action == "P" or action == "p":
            GM.prestige()
            print(GM)
        if action == "R" or action == "r":
            print(GM)