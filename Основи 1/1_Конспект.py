print('Hello World')

#integer (int)
a = 13
a = int(13)

#float (float)
b = 4.2718981898459045
c = 2532.99
b = float(3.141592653589793383462643238279)

#complex
gh = 4 + 6j
gc = 8 - 2.3j
g = complex(4, -2)

ya = float(a)
yb = int(b)
yc = complex(c)

#string (str)
c = 'Hi, I am Artur! '

#boolean (bool)
d = True
e = False
d1 = bool(True)  # True
d2 = bool(1)     # True
d3 = bool(0)     # False
d4 = bool(2.7)   # True
d5 = bool(-295)  # True
d6 = bool('True')   # True
d7 = bool('False')  # True
d8 = bool('')       # False
d9 = str(True)      # 'True'
d10 = str(False)    # 'False'

#Nonetype - нічого
f = None

#Char (ASCII)
print( chr(a) )   #####


'# - коментар'
 # - коментар
'''Багато-рядковий 
коментар'''

del d # Виалення змінної "d"


# Обмін двох змінних значеннями :
var1 = 3
var2 = 14

# 1)
var1, var2 = var2, var1

# 2)
var_temp = var1
var1 = var2
var2 = var_temp


sum = a + b # Додаванняд 
riz = a - b # Віднімання
mno = a * b # Множення
dil = a / b # Ділення
un = -b # Унарний мінус
st = a ** 2 # Зведення числа в степінь
dn = a // 4 # Ділення числа націло
zl = a % 3 # Залишок від ділення числа націло
b += 2 # Cкорочений запис, додавання до числа цифри 2 ( b = b + 2)
b -= 2 #Cкорочений запис, віднімання від числа цифри 2 ( b = b - 2)
b *= 2 # Cкорочений запис, множення числа на 2 ( b = b * 2)
b /= 2 # Cкорочений запис, ділення числа на 2 ( b = b / 2)
b **= 2 # Cкорочений запис, занесення числа в 2  степінь ( b = b ** 2)
b //= 2 # Cкорочений запис, ділення націло на 2 ( b = b // 2)
b %= 2 # Cкорочений запис, залишок від ділення на 2 ( b = b % 2)

print(42.2 - 22)  #  20.200000000000003   -   похибка при рахуванні в пайтоні


# Округлення числа  
k = 4.555555436356346
print('%.2f' % k)  #  4.56
print('%.0f' % k)  #  5
print('%.1f' % k)  #  4.6
print('%.5f' % k)  #  4.55556


v = input("Введіть будь-яке число: ") # Введення даних 

print(c, "I am 16 y.o. !") # Вивід даних на екран (запис окремих елементів через кому)
print(c + str(a)) # "str()" - зміна типу даних
print(a + b + int(v)) # Зміна типу введених даних
print(''' Що ти 
робиш ?''') # Перенесення елемента на наступну строку

print('Як тебе \nзвати?') # Перенесення елемента на наступну строку
print(r'Як тебе \nзвати?') # В такому випадку методи з ' \ ' не будуть проводитись
print(R'Як тебе \nзвати?') # В такому випадку методи з ' \ ' не будуть проводитись

dataf = r"C:\Windows\temp\network\new_file.txt"
print(dataf.split('\\'))   #  ['C:', 'Windows', 'temp', 'network', 'new_file.txt']

print('''Наш список :
/t*Номер один
/t*Номер два
/t*Номер три
''')    # \t = "    "(4 пробєла)

print('Я люблю шоколад "Рошен"') # Запис в лапках
print("А ти любиш шоколад \"Рошен\"") # Запис в лапках
print("Привіт \n" * 3) # Спам певного текстового елементу

print(3 > 5) # Якщо умова "прінта" вірна, вивести "True" , інакше вивести "False"

if not  (10 == 11): # Якщо умова вірна, тоді:
    print(d)     # Вивести змінну "d"

# Якщо умова вірна, тоді виконати певну дію:
if ((a>=b) or (a<=b) and (b>0)) or (a!=b) : # "and - i", "or - чи", "not - не"
    print('Program is good!') # Більше(>) , менше(<) , дорівнює(==), не дорівнює(!=),
                              # Більше або рівно(>=), менше або рівно(<=).


st1 = "Artur"
st2 = "Arturchik"
if ( st1 > st2):
    print(st1, " > ", st2)
elif ( st1 < st2):
    if  a == b :
        print(st1, " < ", st2)
    else:
        print('Noooou!')
else:
    st1, " = ", st2


test = True
while test:
    print("hello")
    test = False

i = 1
while i <=5:
    print(i)
    i = i + 1
    
k = 1
while 1 == 1: #Бескінечний цикл
    print('Привет', + k)
    k += 1
    if k == 3:
        break # Зупинись!

number = 0
while number <= 4:
    number += 1
    if (number % 2) != 0:
        continue;
    print('Парне число' + str(number))



# List :

Mas = [2, 3, 1, 5, 4] # Масив (0,1,2,3,4...)
print( Mas[3]) # Виведення 4-го елементу масиву (який під номером - 3)
Mas.append(6) # Добавлення до масиву значення "6"
Mas.remove(5) # Видалення в масиві значення "5"
Mas.insert(2,0) # Добавлення до масиву елемента "0" на порядковий номер елементу масиву "2"
Mas.reverse() # Відзеркалення масиву відносно свого ценрту
Mas.extend([1, 2, 3])
print(Mas) # Виведення масиву

cv1 = [4]
cv2 = cv1
cv1.append(29)
print(cv1)  # [4, 29]
print(cv2)  # [4, 29]

cv1 = [4]
cv2 = cv1.copy()
cv1.append(29)
print(cv1)  # [4, 29]
print(cv2)  # [4]


Mas2 = [1, 2, 3, 4, [2, 3, 4]] # Створення масиву 'Mas2'
print( Mas2[4] ) # Виведення на екран 5(4)-го елементу масиву 'Mas2'
print( Mas2[4][1] ) # Виведення на екран 2-го елементу в 5-му елементі масиву 'Mas2'
Mas2[0] = 0
print(Mas2[0])

Mas3 = ['a', 'b', 'c', 'd', 'e'] # Створення масиву 'Mas3'
print( Mas3[2] ) # Виведення на екран 3-го елементу масиву 'Mas3'

if 'd' in Mas3: # Якщо елемент 'd' є в масиві 'Mas3' , то :
    print('d - є в списку') # Вивести на екран напис 'd - є в списку'
if 'k' not in Mas3: # Інакше :
    print('d - немає в списку') # Вивести на екран напис 'd - немає в списку'

word = "Artur"
print( word[3] ) # Виведення на екран 4-го елементу змінної 'word'(u)

print(len(Mas)) # Вивести кількість елементів масиву
print(min(Mas)) # Вивести мінімальне значення в масиві
print(max(Mas)) # Вивести максимальне значення в масиві
print(Mas.count(4)) # Вивести кількість елементів "4" в масиві
Mas.sort() # Відсортувати заданий масив "Mas"
print(Mas) # Виведення масиву
Mas_sorted = sorted(Mas) # Поміщення в новий масив 'Mas_sorted' вже відсортованого масиву 'Mas'
print(Mas_sorted)
Reverse_Mass_sorted = sorted(Mas, reverse=True)

Mas4 = list(range(1,100)) # Функція 'list' поміщує в певний масив чи список, вказані аргументи
print(Mas4) # Вивести на екран масив 'Mas4
Mas5 = list(range(0,101,3)) # Помістити в масив "Mas5" значення від 0 до 100, що діляться на 3
print(Mas5) # Виведення масиву


Mas6 = [1, 2, 3, 4, 5, 6] # Створення масиву 'Mas6'
i = 1
length = len(Mas6) # Присвоєння змінній 'length' числа, яке дорівнює кількості елементів в масиві 'Mas6'
while i <= length: # Створення циклу, який виведе на екран числа від 'i' до числа яке дорівнює довжині масиву 'Mas6'
    print(i)
    i += 1


for i in range(1 , 4): # Створення циклу 'for', який виконає 3 рази наступну дію :
    print("How are you ? ") # Виведе на екран напис 'How are you ?'

for number in Mas6: # Створення циклу 'for' , який виконає наступну дію стільки разів, скільки елементів у масиві 'Mas6':
    print( str(number) + ' !') # Виведе на екран номер кола, яке проходить цикл 'for' та ' !'

for h in range(4): # Створення циклу 'for' , який 3 рази виконає наступну дію :
    print("Hi men!") # Виведе на екран 'Hi men!'


    # Обрізання списків(cutting of lists) :
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

digits2 = digits[2:5] # Обрізання списку від елементу індексом 2(включно з ним) до елементу індексом 5(не включно з ним)
print(digits2)

digits3 = digits[5]
print(digits3)

digits4 = digits[:5]
print(digits4)

digits5 = digits[4:]
print(digits5)

digits6 = digits[::2]
print(digits6)

digits7 = range(2, 19)[3::4]
print(digits7)

digits8 = digits[-5]
print(digits8)

digits9 = digits[-5:-1]
print(digits9)

digits10 = digits[::-1]
print(digits10)
# List - end.



# Dictionary(dict) : 

test = {
    "ключ1" : "Значення1",
    "ключ2" : "Значення2",
    125 : 1.200000005006
}
print(test["ключ2"])
print(test.get("ключ1", "Ключа не знайдено")) # При не знаходженні ключа не вибиває помилку і не зупиняє код !

try:
    print(test["ключ5"])
except KeyError:
    print("Такого ключа не існує !")


if 125 in test:
    print('Існує')
else:
    print('Не існує')



contacts = {
    'Андрій Змієвський' : +1123912391239,
    'Артур Статкевич' : +1123812381238,
    'Роман Залізняк' : +1123871721829
}
testing = input('Введіть кого шукаєм ?')

if testing in contacts:
    print('Контакт знайдений : ' + contacts[testing])
else:
    print('Контакт не знайдений !')


moves = {
    (0, 1) : 'Up',
    (1, 0) : 'Right',
    (0, -1) : 'Down',
    (-1, 0) : 'Left'
}
print(moves[(1, 0)])  # 'Right'



d = {'a': 1, 'b': 2, 'c': 3}

print(d.keys())
print(d.values())
print(d.items())
print(d.get('b'))
print(d.pop('b'))
print(d)

print(d.update({'d': 4}))
print(d)

print(d.popitem())
print(d)

print(d.setdefault('e', 5))
print(d)

print(d.copy())
print(d.clear())

# Dictionary(dict) - end.



# Tuple(кортеж) : 

names = ('John', 'Jake', 'Luke')
print(names)  # ('John', 'Jake', 'Luke')
print(names[2])  # ('Luke')

names2 = 'Artur', 'Korlis', 'Den'
print(names2)  # ('Artur', 'Korlis', 'Den')

names3 = tuple(9, 7)
print(names3)  #  (9, 7)

names4 = tuple()
print(names4)  # 

names5 = ()
print(names5) # 

p1, p2, p3 = 44, 66, 88
print(p3, p1, p2)  # 44, 66, 88

t1 = (1)
t2 = (2, 3)
t3 = (4, 5, 6)

t4 = (t1 + t2 + t3) * 4
print(t4)  # (1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
# Tuple(кортеж) - end.



# Set(сет) :
set_1 = {1, 2, 3}
set_2 = set()
set_3 = set_1.union(set_2)
print(set_1)
print(set_2)
print(set_3)


nato = set(['США', 'Україна', 'Польща'])
if 'Україна' in nato:
    print(True)
else:
    print(False)

nato2 = nato.copy()
nato2.add('Англія')
nato2.issuperset(nato)
nato2.remove('Польща')

print(nato2)



# 2) frozen_set()
frozen_s = frozenset({"Alex", "John"})
print(frozen_s)

new_data = frozenset([1, 3, 4, 7, '32', True, 2, 5, 3, 4, 3, 6])
print(new_data)

# Set(сет) - end.




# Створення власних функцій :
def print_spam(): # Створення функції 'print_spam' , яка виконує наступні дії :
    print('I am spamer') # 3 Рази виводить на екран 'I am spamer'
    print('I am spamer')
    print('I am spamer')

print_spam() # Застосування функції 'print_spam'

def multiply(num): # Створення функції 'multiplay' , яка виконує наступні дії :
    print(num * 2) # Множить введене число на 2

multiply(3) # Застосування функції 'multiplay'

def max(x, y): # Створення функції 'max(x, y)' , яка виконує наступні дії :
    if x > y : # Виводить на екран найбільше з двох введених чисел
        return x # 'return' зупиняє виповнення функції і може виводити певний аргумент цієї функції
    else:
        return y 
x = input('Введіть число 1:')
y = input('Введіть число 1:')
print(max(x, y)) # Застосування функції 'max(x, y)'


def func(): # Створення функції 'func' , яка виконує наступні дії :
    '''Описання функції'''
    print(' Hihihi! ') # Виводить на екран напис 'Hihihi!'

print( func.__doc__ ) # Вивести на екран " Опис до функції 'func' "

my_func = func # Копіювання функції 'func' в змінну 'my_func'
my_func() # Застосування функції 'my_func'
my_func2 = func() # Присвоєння змінній 'my_func' значення якого набуває функція 'func'
print(my_func2)

def hello(name):
    print("Hello " + name + "!")
def my_name():
    return input('Введіть ваше ім\'я: ')
hello( my_name() )


def hello(name):
    print("Hello " + name() + "!")
def my_name():
    return input('Введіть ваше ім\'я: ')
hello( my_name )


x = 50
def func_p():
    global p, w  # Функція global створює змінну або міняє її значення не тільки в локальному блоці, а й у всьому коді
    print('p дорівнює ', p)
    p = 2
    print('Замінюєм глобальне значення p на ', p)
func_p()
print('Значення p дорівнює ', p)


def func_outer():
    k = 2
    print('k дорівнює', k)

    def func_inner():
        nonlocal k  # Функція nonlocal робить значення аргуметна не локальним, тільки в певному блоці кода 
        k = 5
    
    func_inner()
    print('Локальне k змінилось на', k)
func_outer()


def say(message, times = 1): # Якщо не вказати кількість повторів повідомлення(другий аргумент), то цей аргумент прийме значення константи '1' , вказаної раніше
    print(message * times)

say('Привіт !')
say('Світ', 4) # Якщо другий аргумент вказаний, він буде дорівнювати кількості повторів повідомлення


def func_abck(a, b=5, c=10):
    print('a дорівнює - ', a, ', b дорівнює - ', b, 'і с дорівнює - ', c)

func_abck(3, 7)
func_abck(25, c = 24)
func_abck(c = 50, a = 100)


def total(initial = 5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))


def total2(initial = 5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)

total2(10, 1, 2, 3, extra_number = 50)
total2(10, 1, 2, 3,)


# Створення функції super_range()
def super_range(*args, **kwargs):
    answer = []
    count = len(args)
    if count == 1:
        start = 0
        stop = args[0]
        step = 1
    elif count == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif count == 3:
        start = [0]
        stop = args[1]
        step = [2]
    else:
        print('Неправильна кількість параметрів !')
    while start < stop:
        answer.append(start)
        start += step
    if 'format' in kwargs:
        format = kwargs['format']
        if format == 'list':
            return answer
        if format == 'tuple':
            return tuple(answer)
        if format == 'set':
            return set(answer)
    else:
        return answer

s_r = super_range(1, 10)
print(s_r)



# Робота з модулем math

import math # Імпорт модуля 'math'
k = 4.51436 # Створення змінної 'k'
print(math.floor(k)) # Округлення в меншу сторону 
print(math.ceil(k)) # Округлення в більшу сторону
print(round(k)) # Правильне округлення
print(math.pi) # Виведення числа Пі
print(math.sqrt(k)) # Виведення кореня з числа 'k'


import random # Імпорт модуля 'random'
J = random.randint(1, 100) # Знаходження рандомного числа від 1 до 100
print(J) 

from random import randint # Імпорт функції 'randint' з модуля 'random'
J = randint(34,78) # Знаходження рандомного числа від 34 до 78
print(J)

from random import * # Імпорт всього модуля 'random'
print(randint(5,12)) # Знаходження рандомного числа від 5 до 12

from math import sqrt as my_sqrt # Імпорт функції 'sqrt' під назвою 'my_sqrt' з модуля 'math'
print(my_sqrt(k)) # Знаходження кореня з числа 'k'



# Застосування найпоширеніших модулів
import os
print(os.getcwd())


import sys 

print('Аргументи командної строки :')
for i in sys.argv:
    print(i)

print('\n\n Змінна PYTHONPATH містить', sys.path, '\n')


import sys

print(dir(sys))
print(dir())
a = 5
print(dir())
del a
print(dir())



import pyowm

city = input('Введіть місто! ')

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
observation = owm.weather_at_place(city)
w = observation.get_weather()
s = w.get_temperature('celsius')['temp']
print(s)


# Помилки
try:
    print(7 / 0)
except ZeroDivisionError:
    pass # Пропустити
    print('Помилку пропущено 1')


try:
    print(7 / 0)
    lgltxht
except :
    print('Помилку пропущено 2')

try:

    print(7 / 0)
    lgltxht
except SyntaxError:
    print('Помилку пропущено 3')
except :
    print('Помилку пропущено 4')
    raise 

try:
    eval(print(6))
except :
    print('Помилку пропущено 5')

try:
    print(6/0)
except (NameError, SyntaxError, ValueError):
    print('Помилку пропущено 5')
finally: # Незалежно від того, чи знайдено помилку, чи ні - виконати дію :
    print("6 / 0 = ~")
    

p = int(input('Введіть будь-яке число: '))
if p == 3:
    raise TypeError('Тест')


class ArturError(exception):
    pass
# raise ArturError()
    


def exc(text):
    assert text != '' # 'AssertionError'
    print(str(text) + '!')
exc('Hello Worldd')


def test(number):
    assert number > 0, 'Число повинне бути більший за 0 !'
    print(str(number))
test(10)



# Робота з файлами

    # Режим читання 'r'
file = open('text.txt', 'r')
print(file.read())
file.close()


filename = input('Введіть назву файла: ')
file = open(filename, 'r')
print('В цьому файлі - ', len(file.read()), ' символів !')
file.close()


file = open('book.txt', 'r')
strings = readlines()
for string in strings:
    print(string)
file.close()


    # Режим перезапису(створення, перестворення) файла 'w'
file = open('text.txt', 'w')
file.write('Hi man - this is just a document !!!')
file.close()


filename = input('Який файл хочете відкрити(створити)? ')
text = input('Який текст хочете помістити в файл?')
file = open(filename, 'w')
file.write(text)
file.close


file = open('text.txt', 'r')
print( file.read(6) ) # В дужках функції 'read()' можна прописати те, скільки байт з цього файлу нам потрібно прочитати
print( file.read(25) )


    # Режим доповнення файла 'a'
file = open('book.txt', 'a')
file.write('You can read this book later\n')
file.close()


    # Режим бінарного читання 'b' ('rb' , 'wb' , 'ab')
import pickle

shoplistfile = 'shoplist.data.txt'
shoplist = ['Яблуко', 'Манго', 'Морква']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # Поміщаєм наш об'єкт в файл 'shoplist.data'
f.close

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load( f ) #Завантажу'ємо обєкт з файла 'shoplist.data'
print(storedlist)
f.close()

    # Видалення файлів
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'text.txt')
os.remove(path)

    #end.


# Програма для копіювання файлів
filename1 = input('Введіть назву файлу, який потрібно скопіювати:')
filename2 = input('Введіть назву файлу, який хочете створити: ')
file1 = open(filename1, 'r')
file2 = open(filename2, 'w')
file2.write( file1.read() )
file1.close()
file2.close()
print('Копіювання успішно завершено! ')
# End.


with open('text.txt', 'r') as F:
    print(f.read(30))
    
    
with open('text.txt', 'w') as tp:
    print('New Line', file=tp)



pass # Команда яка нічого не робить, для створення пустих файлів, змінних та функцій. Пропуск.


# Форматування рядків:
name = 'Artur'
age = 17
print('Привіт, %s ! \nТобі вже %d років!' % (name, age)) #  %s - string, %d - integer, %f - float.

print('Привіт, {}!\nТобі вже {} років!'.format(name, age))

print('{0}{1}{0}!'.format('abra', 'cad')) # {0, 1, 2, 3, 4...}

print('0:.3'.format(1/3))

input_str = "Jessy"
length = 10
# Jessy*****     <     {0:*<10}
# *****Jesyy     >     {0:*>10}
# **Jessy***     ^     {0:*^10}
print('Hello {0:*^10}!'.format(input_str))
print( ('Hello {0:*^'+str(length)+'}!').format(input_str)) # '  '{0:*^' + str(number) + '}'  '



# Функції для роботи з рядками :
fruits = ['Лимон', 'Ківі', 'Яблуко', 'Ананас', 'Клубніка']
members = 'James,Jonny,Jessie,Jack,John'


fruits2 = fruits # Присвоєння змінній fruits2 змінної fruits (змінна fruits2 при її виводі буде ссилатись на значення змінної fruits)
fruits_copy = fruits[:] # Копіювання ЗНАЧЕНЬ змінної fruits в змінну fruits2 (змінна fruits2 при її виводі буде ссилатись лиш на своє значення)


print(' - '.join(fruits)) # 
print(members.split(',')) # 

url = 'www.codewars.com#1-032$902='
print(url.split('#')[0])

print('Привіт, Петро'.replace('Петро','Вася')) # Функція replace замінює перший, із вказаних аргуметнів, на другий


name = input('Введіть будь-яке ім\'я :')
if(name.startswith('A')): # Функція startswith перевіряє чи з вказаного вами символа чи букви починається певний рядок
    print('Ім\'я начинається з букви - А')
else:
    print('Ім\'я НЕ начинається з букви - А')


name2 = input('Введіть будь-яке ім\'я :')
if(name.endswith('r')): # Функція endswith перевіряє чи на вказаний вами символ чи букву закінчується певний рядок
    print('Ім\'я закінчується на букву - r')
else:
    print('Ім\'я НЕ закінчується на букву - r')


name = 'ANdrEY'
print(name.lower()) # Функція upper переводить букви рядка в нижні1 регістр

name = 'AndrEY'
print(name.upper()) # Функція upper переводить букви рядка в верхній регістр


print(min(4, 65, 54365, 23, -332)) # 
print(max('Artur', 'arturchik', 'Markus', 'Denny')) #

print(abs(-1237)) # 


name = ' artur statkevychh '
print(name.title())
print(name.capitalize())
print(name.rsplit())
print(name.rsplit())
print(name.lstrip())


name = 'ArTur'
print(name.swapcase())
print(name.replace('r', 'b'))


#  END...