import threading


# 1)
data = threading.local()

def get():
    print(data.value)
    
def t1():
    data.value = 111
    get()
    
def t2():
    data.value = 222
    get()


threading.Thread(target=t1).start()
threading.Thread(target=t2).start()


# 2)
data2 = threading.local()


def t3():
    data2.value = {'value': 1}
    print('t3:', data2.value)
    
def t4():
    data2.test = ['test1', 'test2']
    print('t4:', data2.test)


threading.Thread(target=t3).start()
threading.Thread(target=t4).start()



# 3)
data3 = threading.local()


def get_name():
    print(data3.name)


def t5():
    data3.name = threading.current_thread().name
    get_name()


def t6():
    data3.name = threading.current_thread().name
    get_name()


threading.Thread(target=t5).start()
threading.Thread(target=t6).start()