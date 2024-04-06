# docstrings пишуться в Функціях, Модулях та Класах

# 1)
def get_even(lst):
    """
    Функція створює список з парних чисел
    :param lst: -> List
    :return even_lst: -> List
    """
    
    even_lst = []
    for el in lst:
        if el % 2 == 0:
            even_lst.append(el)
    return even_lst


help(get_even)
print(get_even.__doc__)



# 2)
import random

help(random)



# 3)
class Model:
    """
    docstring Model
    """


help(Model)