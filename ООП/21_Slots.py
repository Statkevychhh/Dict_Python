class Point2D:
    __slots__ = ('x', 'y', '__length')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x**2 + y**2) ** 0.5


    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        self.__length = value




# Slots при Унаслідуванні
class Touch2D:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Touch3D(Touch2D):
    __slots__ = 'z',


t = Touch3D(10, 20)
t.z = 30
print(t.x, t.y, t.z)
print(t.__slots__)