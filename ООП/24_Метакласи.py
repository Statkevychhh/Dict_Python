class Meta(type):
    def __init__(cls, name, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs

    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value


class Women(metaclass=Meta):
    title = 'заголовок'
    content = 'вміст'
    photo = 'шлях до фото'
    

w = Women()
print(w.__dict__)



# class Women(metaclass=Meta):
#     title = 'заголовок'
#     content = 'вміст'
#     photo = 'шлях до фото'
    
#     def __init__(cls, name, base, attrs):
#         cls.class_attrs = attrs
#         cls.__init__ = Meta.create_local_attrs