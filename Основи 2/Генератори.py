import datetime, sys
from functools import lru_cache


def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

qty = 1000000535252353253252532

# t1 = datetime.datetime.now()
# list_fibo = [fibonacci(i) for i in range(qty)]
# t2 = datetime.datetime.now()
# dt_list = t2 - t1

# print(sys.getsizeof(list_fibo), 'list_memory')
# print(dt_list, 'list_time')


t1 = datetime.datetime.now()
gen_fibo = (fibonacci(i) for i in range(qty))
t2 = datetime.datetime.now()
dt_gen = t2 - t1 


print(sys.getsizeof(gen_fibo), 'gen_memory')
print(dt_gen, 'gen_time')



print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))
print(next(gen_fibo))




# 2)
@lru_cache
def fibo(n):
    result, a, b = [], 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(type(fibo(5)))



@lru_cache
def fibo2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(type(fibo2(5)))

print(next(fibo2(5)))
print(next(fibo2(5)))
print(next(fibo2(5)))
print(next(fibo2(5)))




# 3.1)
a = [x**2 for x in range(1, 6)]
print(a)

a = iter(a)
print(next(a))
print(next(a))
print(next(a))



b = (x**2 for x in range(1, 6))
print(b)

print(next(b))
print(next(b))
print(next(b))


s = list(b)
print(s)
print(s)   # []



c = (i for i in range(1000000))

# for i in c:
#     print(i)




# 3.2)

def f():
    return [43, 65, 32]


def genf():
    for i in [43, 65, 32]:
        yield i
        

s = genf()
print(s)
print(next(s))   # for i in genf():
print(next(s))   #     print(i)
print(next(s))   #




def fact(n):
    pr = 1
    a = []
    for i in range(1, n+1):
        pr = pr * i 
        a.append(pr)
    return a

print(fact(7))


def fact2(n):
    pr = 1
    for i in range(1, n+1):
        pr = pr * i
        yield pr
    
for i in fact2(7):
    print(i, end=' ')
print()
    
    
    
    
# 4) Генератори set-ів
my_set = {i for i in range(1, 6)}       #  my_set2 = set()
print(my_set, type(my_set))             #  for i in [0, 1, 2, 0, 2]

my_set2 = {i for i in [0, 1, 2, 0, 2]}  #      my_set2.add(i)
print(my_set2, type(my_set2))           #  print(my_set2)


my_set3 = {i+j for i in 'abc' for j in '123'}  
print(my_set3)




# 5) Генератори Словників(dict)
a = { f'{i}' : i**2  for i in range(1, 8)}
print(a)


b = {word:len(word) for word in ['hello', 'hi', 'sea']}
print(b)


data = {
    'Джеф Безос': '177',
    'ІлоН Маск': '126',
    'Бернар АрнО': '150',
    'БіЛл ГейтС': '124',
}

new_data = {key.title():int(value) for key, value in data.items()}
print(data)
print(new_data)
print('\n')



users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [3, 'username', '1234'],
    [53, 'qwerty', '5678'],
]

new_users = {user[0]:user for user in users}
print(new_users)
print(new_users[53])