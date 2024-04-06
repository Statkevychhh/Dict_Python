# ООП

    # 1)
class Car:
    hp = 120

    def tunning(self, power):
        self.hp += power

audi = Car()
bmw = Car()
print(type(bmw))  # Car
print(audi.hp)  # 120

audi.hp = 145
print(audi.hp)  # 145
audi.tunning(123)
print(audi.hp)  # 268


#   2)
class Car:
    
    def __init__(self, name, model, **kwargs):
        self.name = name
        self.model = model
        if 'hp' in kwargs:
            self.hp = kwargs['hp']
        else:
            self.hp = 120

    def tunning(self, power):
        self.hp += power

    def info(self):
        print('My', self.name, self.model, 'has', self.hp, 'HP')

audi = Car('Audi', 'A4 3.0', hp = 320)
bmw = Car('BMW', '320i')

print(audi.hp)
bmw.info()


#   3) Інкапсуляція
class Kettle:
    def turn_on(self):
        print('Нажали кнопку включення')
        self.__boil()
        self.__check_temperature()
        self.__beep()
        self._turn_off()

    def __boil(self):
        print('Розігрівання води')

    def __check_temperature(self):
        print('Перевірка температури води')

    def __beep(self):
        print('Подання звукового сигналу')

    def _turn_off(self):
        print('Автоматичне виключення')

my_kettle = Kettle()
my_kettle.turn_on()

my_kettle._turn_off()
my_kettle._Kettle__beep()


#   4)Унаслідування
class Vehicle:
    
    def __init__(self, name, model, **kwargs):
        self.name = name
        self.model = model
        if 'passenger' in kwargs:
            self.passenger = kwargs['passenger']
        else:
            self.passenger = 1


class Car(Vehicle):
    
    def __init__(self, name, model, **kwargs):
        super().__init__(name, model, **kwargs)
        if 'fwd' in kwargs:
            self.fwd = kwargs['fwd']
        else:
            self.fwd = False


class Plane(Vehicle):
    
    def __init__(self, name, model, **kwargs):
        super().__init__(name, model, **kwargs)
        if 'max_height' in kwargs:
            self.max_height = kwargs['max_height']
        else:
            self.max_height = 10000

Audi = Car('Audi', 'A4 3.0', passenger = 5)
print(Audi.__dict__)
Airbus = Plane('Airbus', 'A320', passenger = 176)
print(Airbus.__dict__)


#   5)Поліморфізм
class Animal:
    legs = 4
    tail = 1

    def voice(self):
        print('Якийсь звук')
    

class Cat(Animal):
    
    def voice(Animal):
        print('Мяв-мяв')

class Dog(Animal):
    
    def voice(Animal):
        print('Гав-гав')

class Bull(Animal):
    
    def voice(Animal):
        print('Муууу')

cat1, cat2 = Cat(), Cat()
dog1, dog2 = Dog(), Dog()
bull1, bull2 = Bull(), Bull()
ani = Animal()

farm_band = [cat1, cat2, dog1, dog2, bull1, bull2, ani]


for i in farm_band:
    i.voice()
