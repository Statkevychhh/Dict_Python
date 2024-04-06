class Cat:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'{self.__class__}: {self.name}'


c = Cat('Мурка')
print(c, end='\n\n')



class Cat2:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f'{self.name}'


c2 = Cat2('Мурчик')
print(c2)
print(repr(c2))
print(str(c2), end='\n\n')



# 2)
class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)
    
    def __abs__(self):
        return list(map(abs, self.__coords))
    

p = Point(1, -2, -8, 5)
print(len(p))
print(abs(p))