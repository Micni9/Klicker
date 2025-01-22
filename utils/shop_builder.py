import math
from .bigdecimal import BigDecimal

def cfg_parse(shop_cfg):
    price = []
    multiplier = []
    for generator in shop_cfg:
        price.append(generator["price"])
        multiplier.append(generator["multiplier"])
    return price, multiplier