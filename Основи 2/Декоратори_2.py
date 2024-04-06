import datetime
import time


def outer(func):
    def inner(self, *args, **kwargs):
        time1 = datetime.datetime.now()
        
        z = func(self, *args, **kwargs)
        time.sleep(3)
        
        time2 = datetime.datetime.now()
        
        print(time2 - time1)
        return z
    return inner


class Some:
    @outer
    def casual1(self, x):
        y = x + 1
        return y


    @outer
    def casual2(self, x):
        y = x + 1
        return y


    @outer
    def casual3(self, x):
        y = x + 1
        return y

s = Some()

s.casual1(5)
s.casual2(34)
s.casual3(5392879328)