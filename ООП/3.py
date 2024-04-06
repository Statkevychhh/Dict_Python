class Point:
    "Описання класу Point"
    color = 'red'
    cicle = 2
    

print(Point.color, end="\n\n")
print(Point.__dict__, end="\n\n")
print(Point.__doc__, end="\n\n")

a = Point()
print(type(a))
print(isinstance(a, Point))


setattr(Point, 'prop', 1)
setattr(Point, 'type_pt', 2)
setattr(Point, 'color', 'blue')

print(getattr(Point, 'color'))
print(getattr(Point, 'a', False))

del Point.prop

print(hasattr(Point, 'prop'))
print(hasattr(Point, 'cicle'))

delattr(Point, 'type_pt')
print(hasattr(Point, 'type_pt'))
