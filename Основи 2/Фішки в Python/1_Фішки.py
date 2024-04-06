# 1)
from decimal import Decimal

print(0.1 + 0.1 + 0.1)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))



# 2)
import sys

a = [value for value in range(100_000)]
print(f'{sum(a)=}')
print(f'{sys.getsizeof(a)=}\n')

b = (value for value in range(100_000))
print(f'{sum(b)=}')
print(f'{sys.getsizeof(b)=}\n')



# 3)
def get_user_balance(user_id: int):
    balance = 128.2811
    print(f'UserID: {user_id} | Balance: {round(balance, 1)}')
    print(f'UserID: {user_id} | Balance: {balance:.1f}')
    

get_user_balance(10.12)



# 4)
def get_user_status(option):
    status_options = {
        True: 'Active',
        False: 'Banned',
        0: 'Offline',
        1: 'Deleted',
    }
    return status_options[option]

print(get_user_status(0))
print(get_user_status(1))
print(get_user_status(False))
print(get_user_status(True))



# 5)
from typing import TextIO

def write_data(file_path: str):
    with open(file_path, 'w') as f:
        f.write('hehehe')

def write_data(f: TextIO):
    f.write('hehehe')



# 6)
from collections import namedtuple
from typing import NamedTuple


user_info = ('Alex', 17, True)

print(user_info[0])
print(user_info[1])
print(user_info[2], end='\n\n')



UserInfo = namedtuple('UserInfo', 'name, age, status')
a = UserInfo(name='Alex', age=17, status=True)

print(a.name)
print(a.age)
print(a.status, end='\n\n')



class UserInformation(NamedTuple):
    name: str = 'default'
    age: int = 0
    status: bool = True
    
    def get_info(self) -> str:
        return f'{self.name=}, {self.age=}, {self.status=}'
    
a = UserInformation(name='haha', age=1, status=False)
print(a.name)
print(a.age)
print(a.status)
print(a.get_info())



# end...