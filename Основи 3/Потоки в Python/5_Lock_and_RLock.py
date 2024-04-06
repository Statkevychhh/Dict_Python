# 1) Lock
import threading


locker = threading.Lock()

def inc_value():
    print('Блокіруємо Поток..')
    locker.acquire()
    print('Поток розблокований..')
    
    
t1 = threading.Thread(target=inc_value)
t2 = threading.Thread(target=inc_value)
t1.start()
t2.start()



# 2 ) RLock
locker2 = threading.RLock()

def inc_value2():
    print('Блокіруємо Поток..')
    locker2.acquire()
    print('Поток розблокований..')
    
    
t3 = threading.Thread(target=inc_value2)
t4 = threading.Thread(target=inc_value2)
t3.start()
t4.start()