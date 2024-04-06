import multiprocessing
import time


lock = multiprocessing.Lock()

def get_value(l):
    l.acquire()   # Blocks processing for other processes (Use method 'release()' to unblock!)
    pr_name = multiprocessing.current_process().name
    l.release()   # UnBlocks processing for other processes
    print(f'Процес [{pr_name}] запущений.')



if __name__ == '__main__':
    multiprocessing.Process(target=get_value, args=(lock,)).start()
    multiprocessing.Process(target=get_value, args=(lock,)).start()