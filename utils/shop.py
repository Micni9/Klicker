from .shop_builder import *
from .utils import geometric_sum
from math import floor
from .debug import Debug
from .bigdecimal import BigDecimal

class Shop:
    def __init__(self,item_count,shop_cfg,mode = "SINGLE"):
        self.buy_mode = mode
        self._count = [1]*item_count
        self._base_price, self._multiplier = cfg_parse(shop_cfg)
        self._price = self._base_price.copy()
        self.item_count = len(self._price)
        self._bought_count = [0]*self.item_count
        self._total_price = self._base_price.copy()
        
    def __str__(self):
        shop_str = "*"*23+"SHOP"+"*"*23 + f"\nPrice for buying {self.buy_mode} items:\n"
        for i,price in enumerate(self.total_price):
            shop_str += f"Item {i+1}: {price}\n"
        shop_str += "*"*50
        return shop_str
    
    @property
    def count(self):
        return self._count.copy()
    
    @property
    def price(self):
        return self._price.copy()
    
    @property
    def multiplier(self):
        return self._multiplier.copy()
    
    @property
    def total_price(self):
        return self._total_price.copy()
    
    @property
    def bought_count(self):
        return self._bought_count.copy()
    
    def _calculate_total_price(self,idx:int):
        self.total_price[idx] = geometric_sum(self.price[idx],self.multiplier[idx],self.count[idx])
        
    def set_price(self,idx:int,price:int):
        self._price[idx] = price
        self._calculate_total_price(idx)
    
    def set_mode(self,mode:str):
        self.buy_mode = mode
    
    def set_count(self,idx,count):
        self._count[idx] = count
    
    def set_bought_count(self,idx,amount):
        self._bought_count[idx] += amount
    
    def reset_price(self):
        self._price = self._base_price.copy()
        for idx in range(self.item_count):
            self._calculate_total_price(idx)
    