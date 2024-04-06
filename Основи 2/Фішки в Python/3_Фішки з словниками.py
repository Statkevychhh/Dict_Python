import copy
# Особливості словників
a = {
    "ip": "127.0.0.1",
    "port": (4000),
    ("port"): {
        "id": "123"
    }
}

print(a)
print(a["port"]["id"])


def get_dict() -> dict:
    res = {"1": 1,  "2": 2}
    return dict(res, Amanda=27, Teresa=38, Paula=17, Mario=40)

a: dict = get_dict()
print(a)


a = dict([('Amanda', 27), ('Teresa', 38), ('Paula', 17), ('Mario', 40)])
print(a)


a = {
    "name": "alex"
}
print(a.get("nameless"))   # None


a['age'] = 17
a['name'] = 'Artur'
print(a)



a.update(
    {"name": "Alisa"}
)
a["age"] += 7

print(a)



a["status"] = "87_88_635"
print(a)
del a["status"]   # with error if no key not exist
print(a)

a["status"] = "83_86_225"
print(a)
b = a.pop("status", "Заявка обробляється")
print(a)


print("age" in a)
print("age" not in a)


# NOT Right
b = a
b["age"] = 222
print(a)
print(b)
a["age"] = 19

# Right

b = a.copy()
b["age"] = 127
print(a)
print(b)



a = {
    'name': 'Artur',
    'age': [15, 22],
    'status': True
}
res = copy.deepcopy(a)
res['age'][0] = 1111

print(a)
print(res)


print(len(a))



for x in a.keys():
    print(x)
    
for y in a.items():
    print(y)
    


# Генератори
iters = ['name', 'age', 'value']
values = ['alex', 17, '121']

res = {i: values[num] for num, i in enumerate(iters)}
print(res)



res = [
    {i: values[num] for num, i in enumerate(iters)}
    for _ in range(10)
]
print(res)



# Dict in dict
a = {
    "names": {
        'alex': {
           'age': 20,
           'status': 'Men'
        },
        
        'Elizabet': {
            'age': 23,
            'status': 'Women'
        }
    }
}



# Data_Frame
import pandas as pd
df_index =  pd.DataFrame({'name' : ['Mario', 'Violetta', 'Paula'],
                          'age': [22, 27, 19],
                          'grades': [9, 8.5, 7]},  index=['student_1', 'student_2', 'student_3'])
print(df_index)