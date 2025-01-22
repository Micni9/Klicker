from .bigdecimal import BigDecimal
from .debug import *


class Generator:
    def __init__(self,count=0,multiplier=1,bought_count=0):
        self._count = BigDecimal.to_bigdecimal(count)
        self._multiplier = BigDecimal.to_bigdecimal(multiplier)
        self.bought_count = BigDecimal.to_bigdecimal(bought_count)
    
    def __str__(self):
        return f"Count: {self._count} (x{self._multiplier})"
    
    def __repr__(self):
        return f"Generator: {self._count} (x{self._multiplier})"
    
    def add(self,amount):
        self._count += amount
        
    def increment_bought(self):
        self.bought_count+=1
        self.add(1)
    
    def destroy(self,amount):
        if self.count >= amount:
            self.count -= amount
            return True
        return False
        
    def apply_multi(self,multiplier):
        self._multiplier = self._multiplier*multiplier
        
    @property
    def multiplier(self):
        return self._multiplier.copy()
    
    @property
    def count(self):
        return self._count.copy()
    
    def reset(self):
        self._count = BigDecimal(0)
        self._multiplier = BigDecimal(1)
        self.bought_count = BigDecimal(0)

    @staticmethod
    def generate_generator_list(generator_count:int):
        return [Generator() for _ in range(generator_count)]