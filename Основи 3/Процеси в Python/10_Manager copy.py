import time
import random
import multiprocessing
from multiprocessing import Process, Manager



def func(m_dict, m_list):
    m_dict['name'] = 'test'
    m_dict['version'] = 1.0
    m_list.append(1)
    m_list.append(3)



if __name__ == '__main__':
    with Manager() as m:
        d = m.dict()
        l = m.list()
        pr = Process(target=func, args=(d, l,))
        pr.start()
        
        pr.join()
        print('dict: ', d)
        print('list: ', l)