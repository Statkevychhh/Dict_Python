class Figure:
    def get_pr(self):
        raise NotImplementedError('В дочірньому класі повинен бути переоприділений метод get_pr()')
    

class Rectangle(Figure):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def get_pr(self):
        return 2*(self.w + self.h)
    

class Square(Figure):
    def __init__(self, a):
        self.a = a 
        
    def get_pr(self):
        return 4*self.a
    

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def get_pr(self):
        return self.a + self.b + self.c



figures = [Rectangle(1, 2), Rectangle(3, 4),
           Square(10), Square(20),
           Triangle(1, 2, 3), Triangle(4, 5, 6)]

for f in figures:
    print(f.get_pr())