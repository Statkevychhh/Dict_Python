import multiprocessing
import time


event = multiprocessing.Event()

def test():
    print('Функція test  запущена!')
    while True:
        event.wait()
        print('test')
        time.sleep(1)

  
def test_event():
    while True:
        time.sleep(5)
        event.set()
        print('Event True')
        time.sleep(5)
        event.clear()
        print('Event False')
        


if __name__ == '__main__':
    multiprocessing.Process(target=test).start()
    multiprocessing.Process(target=test_event).start()