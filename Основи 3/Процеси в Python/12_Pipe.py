from multiprocessing import Process, Pipe



def send_data(con):
    con.send('Hello world!')
    con.send(32)
    con.close()


def send_data2(con):
    con.send('Hello 2')
    con.close()



if __name__ == '__main__':
    output_c, input_c = Pipe()
    a = Process(target=send_data, args=(input_c,))
    a.start()
    b = Process(target=send_data2, args=(input_c,))
    b.start()
    
    a.join()
    print('data: ', output_c.recv())
    print('data: ', output_c.recv())
    b.join()
    print('data2: ', output_c.recv())