class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'
    
    def square(self, value):
        self._width = value
        self._height = value
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value


# class Square(Rectangle):
#     def __init__(self, size):
#         Rectangle.__init__(self, size, size)
    
#     @Rectangle.width.setter
#     def width(self, value):
#         self._width = self._height = value
    
#     @Rectangle.height.setter
#     def height(self, value):
#         self._height = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

# sq = Square(5)
sq = Rectangle()
sq.square(5)
use_it(sq)