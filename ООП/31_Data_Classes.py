from dataclasses import dataclass, field

class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
    
    def __repr__(self):
        return f'Thing: {self.__dict__}'


t = Thing('Книга по Python', 100, 1024)
print(t)
print(t.__dict__)
print()



#  2) Data-Class
@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)


td = ThingData('Книга по Python', 90)
print(td)
print(td.__dict__)
print()

td_2 = ThingData('Книга по Python', 80, 512)
td_3 = ThingData('Книга по Python', 80, 512)
print(td == td_2)
print(td_3 == td_2)