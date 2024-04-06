import multiprocessing
import time


def test():
    for _ in range(8):
        print(f"{multiprocessing.current_process().name} - {time.time()}")
        time.sleep(1)
    
    

if __name__ == '__main__':
    a = multiprocessing.Process(target=test, name="prc-1", args=())
    a.start()   # start process
    b = multiprocessing.Process(target=test, name="prc-2")
    b.start()
    print('Процес запущений')
    print(a.is_alive())   # Is process working?  (True or False)
    print(a.pid)
    
    time.sleep(5)
    a.terminate()   # Kill process
    print(a.is_alive())
    print(b.is_alive())
    
    
    a.join()   # command works, after death of this process 
    print('Процес "a" - завершений!')
    b.join()
    print('Процес "b" - завершений!')
    
    
    
    prc = []
    for _ in range(3):
        pr = multiprocessing.Process(target=test)
        prc.append(pr)
        pr.start()
    
    
    for i in prc:
        i.join()
    print('Всі процеси завершені!')