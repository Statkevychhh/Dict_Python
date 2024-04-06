import time
import random
import multiprocessing
from multiprocessing import Process, Barrier


b = Barrier(5)

def f1(bar):
    name = multiprocessing.current_process().name
    sl = random.randint(2, 10)
    print(f'[{name}] - спимо {sl} секунд!')
    time.sleep(sl)
    bar.wait()
    print(f'[{name}] - запущено!')



if __name__ == '__main__':
    for i in range(10):
        Process(target=f1, args=(b,)).start()
    
    # for i in range(8):
    #     Process(target=f1, args=(b,)).start()