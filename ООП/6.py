from typing import Any


class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def set_coords(self, x, y):
        if Point.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    
    
    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left
        
        
    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError("Доступ заборонений.")
        return object.__getattribute__(self, item)
    
    
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Недопустиме ім\'я атрибута')
        print('__setattr__')
        
        self.__dict__[key] = value
        
        object.__setattr__(self, key, value)
    
    
    def __getattr__(self, item):
        print('__getattr__: ' + item)
        return False


    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)



pt1 = Point(1, 2)
# pt2 = Point(10, 20)
# pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.__dict__)


pt1.y = 7
print(pt1.y)


a = pt1.y
print(a)

del pt1.x
print(pt1.__dict__)