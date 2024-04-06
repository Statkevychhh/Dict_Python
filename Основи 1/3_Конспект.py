# Помилки :

try:
    text = input('Введіть що небудь :')
except EOFError:
    print('Ну навіщо ви допустили EOFE ?')
except KeyboardInterrupt:
    print('Ви відмінили операцію !')
else:
    print('Ви ввели {0}'.format(text))


# Створення своїх помилок :
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast 


try:
    text = input('Введіть який-небудь текст :')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Ну навіщо ви допустили EOFE ?')
except ShortInputException as ex:
    print('ShortInputException: Довжина введеного рядка - {0}; \
    очікувалось як мінімум - {1}'.format(ex.length, ex.atleast))
else:
    print('Не було помилок! \n', text)



# Оператор Finally :
import time

try:
    f = open('text.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end= ' ')
        time.sleep(2)
except KeyboardInterrupt:
    print(' !! Ви відмінили читання файла !!')
finally:
    f.close()
    print('(Очистка: Закриття файла)')



# Оператор with :
with open('text.txt') as f:
    for line in f:
        print(line, end='')



# Числа з підкресленням :
k1 = 45675828903
k2 = 45_675_824_903

print(type(k1))
print(type(k2))
print(type(k1)==type(k2))


# eval(), exec() :
y = eval('5 * 3')  # Виполняє int,char() функції й команди
print('y =', y)

exec('u = 4 ** 5')  # Виполняє 'str()' функції й команди
exec('print("Hello World!")')


# Еліпсис  '...', 'Ellipsis'
print(bool(...))  # True
print(bool(None))  # False

qw = [1, 2, 3]
qw[0] = qw
print(qw)  # [[...], 2, 3]


# Нарізка масива 'numpy' :
import numpy as np

sl = np.arrange(16).reshape(2, 2, 2, 2)

print(sl[..., 0].flatten())
print(sl[:, :, :, 0].flatten())


# Цикл For ... else :
letters = [1, 2, 3]

for let in letters :
    print(let)
else :
    print('\nFinish..')


# Модуль sys :
import sys, warnings

sys.version_info
sys.version_info[0] >= 3

if sys.version_info[0] >= 3 :
    warnings.warn('Для роботи цієї програми потрібен Python версії мінімум 3.0', 
          RuntimeWarning)
else :
    pass


# Модуль logging
import os, platform, logging 

if platform.platform().startswith('Windows') :
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
                                os.getenv('HOMEPATH'), \
                                    'test.log')
else :
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Сохраняєм лог в ', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug('Початок програми')
logging.info('Якісь дії')
logging.warning('Програма вмирає')


# Передача кортежів
    # 1)
def get_error_details():
    return (2, 'опис ошибки No2')

errnum, errstr = get_error_details()
print(errnum)
print(errstr)


    # 2)
a, *b = [1, 2, 3, 4]
print(a)  # 1
print(b)  # [2, 3, 4]


    # 3)
c = 5; d = 8
c, d = d, c
print(c)
print(d)


# Метод symmetric_difference
x = {'1', '2', '3'}
y = {'4', '5', '1'}
z = x.symmetric_difference(y)
print(z)


# Оператор (if .. :) :
flag = True
if flag : print('Да')



# Lambda форми (функції)
points = [ { 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 } ]
points.sort(key=lambda i : i['y'])
print(points) 


# Генератори списків
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)


# Передача кортежів і словарів в функції
def powersum(power, *args):
    total = 0
    for x in args:
        total += x**power
    return total
    

powersum(2, 3, 4)  # 25
powersum(2, 10)  # 100



# Оператор assert
#   1)
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()


#   2)
mylist = ['item']
try:
    assert len(mylist) > 1
except AssertionError:
    print('len(mylist) not > 1 !!!')    
mylist.pop()



# Оператор repr
i = []
i.append('item')

repr(i)  #  "['item']"
eval(repr(i))  #  ['item']
eval(repr(i)) == i  # True


# end.

    #
def num_limit(num):
    if num > 255:
        return 255
    elif num < 0:
        return 0
    else:
        return num


def rgb(r, g, b):
    return '{:02X}{:02X}{:02X}'.format(num_limit(r), num_limit(g), num_limit(b)) 
    #


    #
def rgb(k):
    hh = k // 3600
    mm = (k % 3600) // 60
    ss = k % 60
    return '{:02d}{:02d}{:02d}'.format(hh, mm, ss) 
    #

# Lambda - функції:

def f(x,y):
    return (x + y)**2

def f(x,y):    return (x + y)**2

l = lambda x, y: (x + y)**2
(lambda x, y: (x + y)**2)(2,7)

# Example:

users = [
    "Artur Grey 32",
    "John Dick 61",
    "Camel Srowvy 19",
    "Den Ueben 37",
    "Fally Bor 24",
    "Heyy Sem 45"
]

users.sort(key = lambda x: x.split(' ')[-1])
print(users)

# Методи-прискорювачі

    # 1)map:
measures = [
    (15, 10),
    (14, 22),
    (11, 13),
    (10, 20),
    (15, 17),
]

p = [w_l[0] * w_l[1] for w_l in measures]

m = map(lambda w_l: w_l[0] * w_l[1], measures)  # Отримаємо об'єкт класу map
print(m)


    # 2)filter:
f = filter(lambda w_l:  w_l[0] * w_l[1] < sum(p)/len(p), measures)
print(f)


    # 3)reduce
massive = [1, 2, 3, 4, 5]
#reduce(lambda x,y: x+y, massive)



# Функції-справочники

#   1)type
a = 79
print(type(a))

#   2)vars
b = ShortInputException()
print(vars(b))

#   3)dir
print(dir(b))

#   4)mro
print(ShortInputException.mro())

#   5)help
help(b)


# END.