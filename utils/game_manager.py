from .currency import Currency
from .generator import Generator
from .utils import *
from .game_manager_builder import *
from .debug import *
from .bigdecimal import BigDecimal
from math import sqrt

class GameManager:
    def __init__(self,cfg,generator_cfg):
        self._starting_coins = cfg['starting_coins']
        self._starting_gems = cfg['starting_gems']
        self.gem_bonus = cfg['gem_bonus']
        
        self.multi_stage = cfg['multi_stage']
        self.multi_jump = cfg['multi_jump']
        self.generator_count = cfg['generator_count']
        self.base_generate_amount = cfg['base_generate_amount']
        
        self.generator_list = Generator.generate_generator_list(self.generator_count)
        self.price = generator_cfg["price"]
        self.isAffordable = None
        self._next_stage = None
        self.currency = None
        
        self.isRunning = False
        
    @property
    def score(self):
        score = self.currency.coins
        for n,generator in enumerate(self.generator_list):
            score += generator.count * (2**(n+1))
        return score
        
    def __str__(self):
        game_str = str2title("currency")
        game_str += str(self.currency)+ '\n'
        game_str += str2title("generator")
        for i in range(self.generator_count):
            game_str += f"Generator {i+1}: {self.generator_list[i]}\n"
        game_str += str2title("")
        return game_str
        
    def game_start(self,starting_coins=None,starting_gems=None):
        if starting_coins is None:
            starting_coins = self._starting_coins
        if starting_gems is None:
            starting_gems = self._starting_gems
        self.currency = Currency(starting_coins,starting_gems,self.gem_bonus)
        self._update_affordability()
        self._reset_next_stage()
        self.isRunning = True
    
    def _update_affordability(self):
        self.isAffordable = [self.currency.coins >= p for p in self.price]
    
    def to_next_stage(self,idx)->int:
        jump_idx = -1
        for i,jump in enumerate(self.multi_jump):
            if self._next_stage[idx] < jump:
                break
            jump_idx = i
        if jump_idx == -1:# amount_now < 25
            self._next_stage[idx] = BigDecimal(self.multi_stage[0])
        else:
            # amount_now >= 25
            self._next_stage[idx] +=  self.multi_stage[jump_idx]
    
    def _reset_next_stage(self):
        self._next_stage = [BigDecimal(self.multi_stage[0]) for _ in range(self.generator_count)]
    
    def _update_generator_multiplier(self,idx):
        if self.generator_list[idx].bought_count >= self._next_stage[idx]:
            self.to_next_stage(idx)
            self.generator_list[idx].apply_multi(2)
    
    def buy_generator(self,idx:int):
        if idx >= self.generator_count:
            print("Invalid index")
            return
        if self.isAffordable[idx]:
            self.currency.spend(self.price[idx])
            self.generator_list[idx].increment_bought()
            self._update_generator_multiplier(idx)
            self._update_affordability()
        else:
            pass
    
    def prestige(self):
        earned_gems = (self.score//self.price[-1]).sqrt().floor()
        Display("Prestige",f"You have earned {earned_gems} gems")
        for generator in self.generator_list:
            generator.reset()
        self.game_start()
        
    def _game_tick(self):
        if not self.isRunning:
            return
        gems_multiplier = self.currency.multiplier
        self.currency.earn(self.generator_list[0].count*self.generator_list[0].multiplier*gems_multiplier)
        for i in range(1,self.generator_count):
            self.generator_list[i-1].add(self.base_generate_amount*self.generator_list[i].count*self.generator_list[i].multiplier)
        self._update_affordability()
        
        
        