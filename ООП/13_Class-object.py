class Geom:
    pass


class Line(Geom):
    pass


print(Geom.__name__)

g = Geom()
print(g)

l = Line()
print(l.__class__)

print(issubclass(Line, Geom))      # True
print(issubclass(Geom, Line))      # False
print(issubclass(Geom, object))    # True
print()

print(isinstance(l, Line))      # True
print(isinstance(l, Geom))      # True
print(isinstance(l, object))    # True
print()

print(isinstance(int, object))
print()



# 2)
class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))


s = list([1, 2, 3])
print(s)

v = Vector([1, 2, 3])
print(v)