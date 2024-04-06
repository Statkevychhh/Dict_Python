from dataclasses import dataclass, field, InitVar, make_dataclass
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]

  
@dataclass()
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None
    
    def __post_init__(self):
        print('Goods: post_init')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass()
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)
    
    def __post_init__(self):
        super().__post_init__()
        print('Books: post_init')


b = Book(1000, 100, 'Python ООП', 'Балакіров С.М.')
print(b)

b2 = Book(2000, 30, 'Python ООП', 'Балакіров С.М.')
print(b2)



# 2-й спосіб створення Data-класів
CarData = make_dataclass('CarData', [('model', str),
                                     'max_speed', 
                                     ('price', float, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed})


c = CarData('BMW', 256, 103_000)
print(c)