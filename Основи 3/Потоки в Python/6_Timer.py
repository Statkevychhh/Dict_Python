import threading
import time


def test():
    while True:
        print("test")
        time.sleep(1)
        
        
thr = threading.Timer(5, test)
thr.start()

for _ in range(8):
    print("111")
    time.sleep(1)
    
thr.cancel()



# 2)
def test2():
    while True:
        print("test")
        time.sleep(1)
        
        
thr2 = threading.Timer(5, test2)
thr2.setDaemon(True)
thr2.start()

for _ in range(6):
    print("111")
    time.sleep(1)
    
thr2.cancel()
print('finish')

