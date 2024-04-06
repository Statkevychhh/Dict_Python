import threading 
import time


def sum(a, b):
    print(a + b)
    time.sleep(3)

print(threading.current_thread())    
print(threading.active_count())
    
print(threading.main_thread())
threading.main_thread().setName("Головний поток")
print(threading.main_thread())
    

t = threading.Thread(target=sum, args=(3, 18), kwargs={})
t.start()

print(threading.active_count())
print(threading.enumerate())

t.join()
print('Поток закінчився')



# 2)
def sum(a, b):
    print(a + b)
    

t = threading.Timer(3, sum, args=(6, 11), kwargs={})
t.start()