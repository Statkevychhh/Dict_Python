# Аннотація типів
from typing import List, Dict

name: str = 'Olga'
age: int = 29

friends: List[str] = ['Serega', 'Vovan']



# Аннотація в функціях
def sum_of_numbers(a: int, b: int) -> int:
    return a + b

print(sum_of_numbers(7, 9))



# Аннотація спеціальних (важких) типів
from typing import Union, Final, NoReturn

def car_speed() -> Union[int, float]:
    return 89.6
    
print(car_speed())


MAX_PRICE : Final = 9.99


def greeting() -> NoReturn:
    try:
        1/0
    except ZeroDivisionError:
        print('You can not divide by zero')

# greeting()




# 2)
from typing import Optional, Any, Union


first: int = 100
print(first)
first = 'hello'
print(first)


             #  a: int | float = 7
def add_numbers(a: Union[int, float] = 7, b: Optional[int] = None) -> int:
    return a + b

print(add_numbers(27, 45))
# print(add_numbers())
print(add_numbers('hello', ' world'))
print(add_numbers.__annotations__) 



def list_upper(lst: List[str]):
    for elem in lst:
        print(elem.upper())
        
print(list_upper(['hello', 'hi', 'byebye']))



d: Dict[str, int] = {'a': 100, 'b': 200}


e: Any = 12
e = 'fsdstring'