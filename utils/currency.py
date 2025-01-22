from .bigdecimal import BigDecimal

class Currency():
    def __init__(self, coins,gems,gem_bonus:float):
        self._coins = BigDecimal.to_bigdecimal(coins)
        self._gems = BigDecimal.to_bigdecimal(gems)
        self._multiplier = None
        self.gem_bonus = gem_bonus

    def __str__(self):
        return f"Coins: {self.coins}\nGems: {self.gems}"

    def __repr__(self):
        return f"Coins: {self.coins}, Gems: {self.gems}"
    
    @property
    def multiplier(self):
        if self._multiplier is None:
            self._multiplier = 1 + self.gems*self.gem_bonus
        return self._multiplier.copy()
    
    @property
    def coins(self):
        return self._coins
    
    @property
    def gems(self):
        return self._gems.copy()
    
    def earn(self,amount):
        self._coins += amount
    
    def spend(self,amount):
        if self._coins >= amount:
            self.earn(-amount)
            return True
        return False
    
    def set(self,coins,gems):
        self._coins = BigDecimal.to_bigdecimal(coins)
        self._gems = BigDecimal.to_bigdecimal(gems)
        self._multiplier = None