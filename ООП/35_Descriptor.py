import logging


class Item:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name
    
    def __get__(self, obj, objtype = None):
        value = getattr(obj, self.private_name, None)
        print(f'Got value {self.public_name}: {value}')
        return value

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError(f'Argument must be string')
        print(f'Seted value {self.public_name}: {value}')
        setattr(obj, self.private_name, value)


class Shop:
    book = Item()
    
    def __init__(self, book):
        self.book = book


my_shop = Shop(book='All about among us')
print(my_shop.book)

my_shop.book