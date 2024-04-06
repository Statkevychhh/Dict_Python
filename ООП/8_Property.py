class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
        
    
    @property
    def old(self):
        return self.__old
    
    
    @old.setter
    def old(self, old):
        self.__old = old
    
        
    @old.deleter
    def old(self):
        del self.__old
    

    # old = property(get_old, set_old)  # setter(), getter(), deleter()
    
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person('Сергій', 20)

p.old = 32
print(p.old, p.__dict__)

del p.old
print(p.__dict__)



# Приклад використання об'єктів @property

from string import ascii_letters

class Persona:
    S_UA = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя-'
    S_UA_UPPER =S_UA.upper()
    
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)
        
        self.__fio = fio
        self.__old = old
        self.__passport = ps
        self.__weight = weight
    
        
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФІО повинне бути рядком')
        
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неправильний формат запису')
        
        letters = ascii_letters + cls.S_UA + cls.S_UA_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФІО повинен бути хочаб один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФІО можна використовувати тільки букви та дефіс')
    
    
    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Вік повинен бути цілим числом в діапазоні від 14 до 120')
        
    
    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Вага повинна бути числом від 20')
    
    
    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт повинен бути рядком')
        
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неправильний формат паспорта')
        
        for p in s:
            if not p.isdigit():
                raise TypeError('Серія і номер паспорта повинні бути числами')
    
    
    @property
    def get_fio(self):
        return self.__fio
    
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old
    
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight
    
    
    @property
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps
    

        

p = Persona('Статкевич Артур Андрійович', 17, '1234 567890', 80.0)
print(p.__dict__)

p.old = 100
p.passport = '7890 123456'
p.weight = 70.0
print(p.__dict__)