import math
from .debug import *


class BigDecimal:
    TENTH_STR = ["K","M","B","T"]
    
    def __init__(self,base_num,exponent=0):
        try:
            self.base_num = float(base_num)
        except:
            raise TypeError(f"Invalid type for base number: {type(base_num).__name__}")
        try:
            self.exponent = int(exponent)
        except:
            raise TypeError(f"Invalid type for exponent:{type(exponent).__name__}")
        self.standardize()
        self._str = None
    
    
    def standardize(self):
        if self.base_num == 0:
            self.exponent = 0
        elif self.base_num >= 10 or self.base_num<1:
            n = math.floor(math.log10(abs(self.base_num)))
            self.exponent += n
            self.base_num /= 10 ** n
    
    @staticmethod
    def to_bigdecimal(value):
        if isinstance(value, BigDecimal):
            return value.copy()
        try:
            return BigDecimal(value)
        except TypeError:
            raise TypeError(f"Cannot convert {type(value).__name__} to BigDecimal")
    
    def sqrt(self):
        if self.base_num < 0:
            raise ValueError(f"Cannot compute square root of a negative number: {self.__repr__()}")
        base_num_sqrt = math.sqrt(self.base_num)
        exponent_sqrt = self.exponent / 2
        if exponent_sqrt.is_integer():
            return BigDecimal(base_num_sqrt, int(exponent_sqrt))
        else:
            return BigDecimal(base_num_sqrt * math.sqrt(10), int(exponent_sqrt) - 1)
    
    def copy(self):
        output = BigDecimal(self.base_num,self.exponent)
        output._str = self._str
        return output
    
    def __add__(self,num):
        if not isinstance(num,BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for addition: BigDecimal and {type(num).__name__}")
        if self.__ge__(num):
            max_decimal = self
            min_decimal = num
        else:
            max_decimal = num
            min_decimal = self
        diff_exponent = max_decimal.exponent - min_decimal.exponent
        if diff_exponent > 8:
            return max_decimal.copy()
        base_num_sum = max_decimal.base_num+min_decimal.base_num/(10**diff_exponent)
        return BigDecimal(base_num_sum,max_decimal.exponent)
        
    def __radd__(self,num):
        return self.__add__(num)
    
    def __neg__(self):
        return BigDecimal(-self.base_num, self.exponent)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        return BigDecimal(abs(self.base_num), self.exponent)
    
    def __sub__(self,num):
        if not isinstance(num,BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for subtraction: BigDecimal and {type(num).__name__}")
        return self.__add__(-num)
    
    def __rsub__(self, num):
        if not isinstance(num,BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for subtraction: {type(num).__name__} and BigDecimal")
        return num.__sub__(self)
    
    def __mul__(self, num):
        if not isinstance(num,BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for multiplication: BigDecimal and {type(num).__name__}")
        base_num_product = self.base_num * num.base_num
        exponent_sum = self.exponent + num.exponent
        return BigDecimal(base_num_product, exponent_sum)

    def __rmul__(self, num):
        return self.__mul__(num)
    
    def __iadd__(self, num):
        result = self.__add__(num)
        self.base_num = result.base_num
        self.exponent = result.exponent
        self._str = None
        return self

    def __isub__(self, num):
        result = self.__sub__(num)
        self.base_num = result.base_num
        self.exponent = result.exponent
        self._str = None
        return self

    def __imul__(self, num):
        result = self.__mul__(num)
        self.base_num = result.base_num
        self.exponent = result.exponent
        self._str = None
        return self

    def __itruediv__(self, num):
        result = self.__truediv__(num)
        self.base_num = result.base_num
        self.exponent = result.exponent
        self._str = None
        return self
        
    def __ifloordiv__(self, num):
        result = self.__floordiv__(num)
        self.base_num = result.base_num
        self.exponent = result.exponent
        self._str = None
        return self
    
    def __eq__(self, num):
        if not isinstance(num, BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                return False
        return self.base_num == num.base_num and self.exponent == num.exponent
    
    def __ne__(self, num):
        return not self.__eq__(num)

    def __lt__(self, num):
        if not isinstance(num, BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for comparison: BigDecimal and {type(num).__name__}")
        if self.exponent == num.exponent:
            return self.base_num < num.base_num
        return self.exponent < num.exponent

    def __le__(self, num):
        return self.__lt__(num) or self.__eq__(num)

    def __gt__(self, num):
        return not self.__le__(num)

    def __ge__(self, num):
        return not self.__lt__(num)
    
    def __truediv__(self, num):
        if not isinstance(num, BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for division: BigDecimal and {type(num).__name__}")
        if num.base_num == 0:
            raise ZeroDivisionError("division by zero")
        base_num_quotient = self.base_num / num.base_num
        exponent_diff = self.exponent - num.exponent
        return BigDecimal(base_num_quotient, exponent_diff)

    def __floordiv__(self, num):
        return (self.__truediv__(num)).floor()
    
    def __rtruediv__(self, num):
        if not isinstance(num, BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for division: {type(num).__name__} and BigDecimal")
        return num.__truediv__(self)

    def __rfloordiv__(self, num):
        if not isinstance(num, BigDecimal):
            try:
                num = BigDecimal(num)
            except TypeError:
                raise TypeError(f"Invalid type for integer division: {type(num).__name__} and BigDecimal")
        return num.__floordiv__(self)
    
    def floor(self):
        if self.exponent >= 0:
            return BigDecimal(round(self.base_num,self.exponent+1),self.exponent)
        else:
            return BigDecimal(0)

    @property
    def str(self):
        if self._str is None:
            if self.exponent < 3:
                output_str = "{:.5f}".format(self.base_num*(10**self.exponent))
                self._str = output_str[:6]
            elif self.exponent < 15:
                idx = self.exponent//3-1
                self._str = "{:.4f}{}".format(self.base_num,BigDecimal.TENTH_STR[idx])
            else:
                self._str = "{:.3f}e{}".format(self.base_num,self.exponent)
        return self._str

    def __str__(self):
        return self.str
    
    def __int__(self):
        return int(self.base_num * (10 ** self.exponent))

    def __float__(self):
        return float(self.base_num * (10 ** self.exponent))
    
    def __repr__(self):
        return self.str