print(type(int))
print(type(str))

class B1: pass
class B2: pass

print(type(B1))


def method1(self):
    print(self.__dict__)



class Point:
    MAX_COORD = 100
    MIN_COORD = 0

A = type('Point', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD': 0, 'method1': method1, 'method2': lambda self: self.MAX_COORD})
print(A.__mro__)

pt = A()
pt.method1()
print(pt.method2())