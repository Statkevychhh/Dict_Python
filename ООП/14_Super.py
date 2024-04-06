class Geom():
    name = 'Geom'
     
    def __init__(self, x1, y1, x2, y2):
        print(f'Ініціалізатор Geom для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    name = 'Line'
    
    def draw(self):
        print('Малювання лінії')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
    #   Geom.__init__(self, x1, y1, x2, y2)
        super().__init__(x1, y1, x2, y2)
        self.fill = fill
        
        print('Ініціалізатор Rect')
    
    def draw(self):
        print('Малювання прямокутника')


l = Line(0, 0, 10, 10)
r = Rect(1, 2, 3, 4)
print(r.__dict__)