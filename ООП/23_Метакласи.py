# 1)
def create_class_point(name, base, attrs):
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)

pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())



# 2)
class Met(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)


    # def __init__(cls, name, base, attrs):       # 2-й спосіб
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


class Point2(metaclass=Met):
    def get_coords(self):
        return (1, 1)


pt2 = Point2()
print(pt2.MAX_COORD)
print(pt2.get_coords())