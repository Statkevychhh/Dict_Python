import threading 
import time


print("name:", threading.main_thread().name)
threading.main_thread().setName("result")
print("result:", threading.main_thread().name)


def get_data(data, value):
    for _ in range(value):
        print(f"[{threading.currentThread().name}] - {data}")
        time.sleep(1)
    
    
thr_list = []
for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f"thr-{i}")
    thr_list.append(thr)
    thr.start()

print(thr_list)

for i in thr_list:
    i.join()

print('finish')



# 2) Потоки-Демони

def get_data2(data):
    for _ in range(5):
        print(f"[{threading.currentThread().name}] - {data}")
        time.sleep(1)
        
        
thr2 = threading.Thread(target=get_data2, args=(str(time.time()),), daemon=True)
thr2.setDaemon(True)
thr2.start()
time.sleep(1)
print('finish')
