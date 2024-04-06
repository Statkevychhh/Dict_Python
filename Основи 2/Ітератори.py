# 1)
cars = ['bmw', 'audi', 'mercedes']
# print(cars[0])


it = iter(cars)
print(next(it))
print(next(it))
print(next(it))



# 2)
text = 'abcdef'
# print(text[0])


it = iter(text)
print(next(it))
print(next(it))
next(it)
print(next(it))