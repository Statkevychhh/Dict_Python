import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


s1 = Point(1, 2)
print(s1.__dict__)



class Point2D:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


s2 = Point2D(2, 5)
print(s2.__slots__)
print()

print(s1.__sizeof__() + s1.__dict__.__sizeof__())
print(s2.__sizeof__() + s2.__slots__.__sizeof__())
print()


t1 = timeit.timeit(s1.calc)
t2 = timeit.timeit(s2.calc)
print(f'{t1} seconds')
print(f'{t2} seconds')