class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __len__(self):
        print('__len__')
        return self.x ** 2 + self.y ** 2


p = Point(3, 4)

print(bool(Point(0, 0)))
print(bool(p))



class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __len__(self):
        print('__len__')
        return self.x ** 2 + self.y ** 2

    def __bool__(self):
        print('__bool__')
        return self.x == self.y


p1 = Point2(7, 8)
p2 = Point2(9, 9)
print(bool(p1))
print(bool(p2))