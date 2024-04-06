class Clock:
    __DAY = 86400
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('')
        self.seconds = seconds % self.__DAY
    
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')
    
    
    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правий операнд повинен бути типу int або Clock')
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            
        return Clock(self.seconds + sc)
    
    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правий операнд повинен бути типу int або Clock')
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            
        return Clock(self.seconds - sc)
    
    def __mul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правий операнд повинен бути типу int або Clock')
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            
        return Clock(self.seconds * sc)
    
    def __truediv__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правий операнд повинен бути типу int або Clock')
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            
        return Clock(self.seconds / sc)
    
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        print('__iadd__')
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правий операнд повинен бути типу int або Clock')
        
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        
        self.seconds += sc
        return self
#   '__floordiv__' - '//'
#   '__mod__' = '%')



c1 = Clock(1000)
print(c1.get_time())

c1 += 100
print(c1.get_time())

c2 = Clock(4800)
c3 = c1 + c2
print(c3.get_time())

c3 -= 1200
print(c3.get_time())

c3 *= 6
print(c3.get_time())

c3 = 180 + c3 
print(c3.get_time())