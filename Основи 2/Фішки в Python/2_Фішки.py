# 1
import jmespath

persons = {
    'persons' : [
        { 'name': 'Alex', 'age': 27 },
        { 'name': 'John', 'age': 33 },
        { 'name': 'Rob', 'age': 19 }
    ]
}

result = jmespath.search('persons[*].age', persons)
print(result)



# 2
a = { 'test': { 'a': False}, 'execute': lambda x: print(x)}

a['execute']('Hello World!')



# 3
from collections import Counter

mylist = [1, 1, 1, 2, 3, 4, 4, 'name', 'name']
c = Counter(mylist)
print(c)

print(Counter('aaaaabbbccccc'))



# 4
x = 10

if 5 < x and x < 15:
    print('Yes')
    
if 5 < x < 15:
    print('Yes - 2')
    
    
    
# 5
from dateutil.parser import parse

logline = 'INFO 2020-01-01T00:00:01 Happy new year, human.'
timestamp = parse(logline, fuzzy=True)
print(timestamp)



# 6 
def upper(s):
    return s.upper()

mass = list( map(upper, ['test', 'work']) )
print(mass)   # ['TEST', 'WORK']

list_of_int = list( map(int, '1234567') )
print(list_of_int)   # [1, 2, 3, 4, 5, 6, 7]



# 7
x = 10
res = 1 if x == 9 else 2
print(res)



# 8 
class T:
    def __init__(self):
        print('hello world')
        
a = { 'test': { 'a': False }, 'execute': T() }
b = { 'test': { 'a': False }, 'execute': T }


res = b['execute']()