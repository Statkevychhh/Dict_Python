import time
import threading


value = 0
locker = threading.Lock()

def inc_value():
    global value
    for _ in range(20):
        locker.acquire()
        value += 1
        time.sleep(0.01)
        print(value)
        locker.release()
        
        
        
    for _ in range(5):
        with locker:
            value += 1
            time.sleep(0.01)
            print(value)
    
        
for _ in range(5):
    threading.Thread(target=inc_value).start()



