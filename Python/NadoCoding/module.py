## 모듈 제작
import theater_module
theater_module.price_army(30)
theater_module.price_morning(10)

import theater_module as mv
mv.price(3)

from theater_module import *
price_morning(7)

from theater_module import price, price_morning
price(5)

from theater_module import price_army as price
price(3) # 실제 price_army