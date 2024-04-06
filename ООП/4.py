class Point:
    color = "red"
    circle = 2
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __del__(self):
        print(f"Видалення екземпляра: {str(self)}")
        
    def get_cords(self):
        return self.x, self.y
    
    
pt = Point()
pt2 = Point(3, 5)

print(pt.get_cords())
print(pt2.get_cords())



# 2)

class Point2:
    
    def __new__(cls, *args, **kwargs):
        print(f"Виклик  __new__  для {str(cls)}")
        return super().__new__(cls)
        
        
    def __init__(self, x = 0, y = 0):
        print(f"Виклик  __init__  для {str(self)}")
        self.x = x
        self.y = y
        
pt3 = Point2(1, 2)



# 3)

class DataBase:
    __instance = None
    
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            
        return cls.__instance
        
        
    def __del__(self):
        DataBase.__instance = None        
        
        
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port
        
        
    def connect(self):
        print(f"З'єднання з БД: {self.user}, {self.psw}, {self.port}")
        
            
    def close(self):
        print("Закриття з'єднання з БД")
        
        
    def read(self):
        return "Дані з БД"
        
        
    def write(self, data):
        print(f"Запис даних в БД: {data}")
            
            
db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))


db.connect()
db2.connect()



# 4)
class Vector:
    MIN_CORD = 0
    MAX_CORD = 100
    
    
    @classmethod
    def validate(cls, argument):
        return cls.MIN_CORD <= argument <= cls.MAX_CORD
    
    
    def __init__(self, x, y):
        self.x = self.y = 0
        
        if Vector.validate(x) and self.validate(y):
            self.x = x
            self.y = y
            
        print(self.norm_2(self.x, self.y))
        
    
    def get_cords(self):
        return self.x, self.y
    
    
    @staticmethod
    def norm_2(x, y):
        return x*x + y*y
    


print(Vector.validate(5))

v = Vector(10, 20)
print(Vector.norm_2(5, 7))
res = v.get_cords()   #res = Vector.get_cords(v)
print(res)