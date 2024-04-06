from threading import Thread, current_thread, BoundedSemaphore
import time, random
import threading



# 1) Semaphore
max_connect = 5
pool = BoundedSemaphore(value=max_connect)


def test():
    with pool:
        slp = random.randint(1, 5)
        print(f"{current_thread().name} - sleep ({slp})")
        time.sleep(slp)
            
    
for i in range(10):      
    Thread(target=test, name=f'thr-{i}').start()
    
    
    
# 2) Barier
bar = threading.Barrier(5)

def test2(barier):
    slp = random.randint(3, 7)
    print(f"Поток [{current_thread().name}] - запущений в ({time.ctime()})")
    time.sleep(slp)
    
    barier.wait()
    print(f"Поток [{current_thread().name}] - перетнув бар'єр в ({time.ctime()})")


for i in range(0, 5):
    threading.Thread(target=test2, args=(bar,), name=f"thr-{i}").start()

