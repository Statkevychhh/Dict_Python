import datetime
import time


def outer(func):
    def inner(*args, **kwargs):
        time1 = datetime.datetime.now()
        
        z = func(*args, **kwargs)
        time.sleep(3)
        
        time2 = datetime.datetime.now()
        
        print(time2 - time1)
        return z
    return inner


@outer
def casual1(x):
    y = x + 1
    return y


@outer
def casual2(x):
    y = x + 1
    return y


@outer
def casual3(x):
    y = x + 1
    return y

print(casual1(5))
print(casual2(9))
print(casual3(232213))
