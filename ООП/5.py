from accessify import private, protected

class Point:
    
    def __init__(self, x, y, value):
        self.value = value   #public
        self._value2 = value   #_protected
        
        if self.__check_value__(x) and self.__check_value__(y):
            self.__x = x   #__private
            self.__y = y   #__private
        
       
    @private
    @classmethod
    def __check_value__(cls, x):
        return type(x) in (int, float)
     
        
    def set_coord(self, x, y):  #  Сеттер
        if self.__check_value__(x) and self.__check_value__(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координати повинні бути числами")
        
    def get_coord(self):        #  Геттер
        return self.__x, self.__y
        
        
pt = Point(1, 2, 7)

print(pt.value)
print(pt._value2)

# print(pt.__x, pt.__y)  # - AttributeError
print(pt._Point__x, pt._Point__y) # - Не потрібно так звертатись!!!


pt.set_coord(10, 20)
print(pt.get_coord())