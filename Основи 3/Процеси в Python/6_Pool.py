import multiprocessing
import random



def end_func(response):
    print('Завдання завершено!')
    print(response)


def get_value(value):
    name = multiprocessing.current_process().name
    print(f'[{name}] value: {value}')
    return value


def end_func2(response):
    print(f'end_func2: {response}')
    

def out(x):
    print(f'value: {x}')
    return x
    

def out2(x, y, z):
    print(f'value: {x} {y} {z}')


def end_func3(response):
    print('end_func3: ', response)


def out3(x, y, z):
    print(f'value: {x} {y} {z}')
    return x, y, z
    


if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.map(get_value, list(range(5)))
    
    
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.map_async(get_value, list(range(20)), callback=end_func)
        p.close()
        p.join()
        
        
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        for i in range(10):
            p.apply_async(out, args=(i,), callback=end_func2)
        p.close()
        p.join()
        
        
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap(out2, [(1, 2, 3), (4, 5, 6)])
        
        p.close()
        p.join()
        
        
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap_async(out3, [(1, 2, 3), (4, 5, 6)], callback=end_func3)
        
        p.close()
        p.join()
