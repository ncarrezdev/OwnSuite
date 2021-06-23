'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from DevTools.preppend_py_files_header import preppend_py_files_header
preppend_py_files_header()


if __name__ == '__main__':
    from time import sleep 

    from OwnSuite import Data, Array, Dictionary, Enum, StateMachine, Random, Encryption, Thread
    from Compression import *

    class E_ENUM(Enum):
        v = 0
        b = 1
        a = 2

    def event_called():print('Event Called')

    d = Data(0)
    print(d)
    e = Data(0, features=('event',))
    print(e)

    a = Array([0,1,2,3,4,5])
    print(a)

    d = Dictionary()
    d.append('ma_clef', 'ma_val')
    print(d)

    print(E_ENUM)

    s = StateMachine(['start','quit'])
    print(s)

    print(Random.random(0, 10))

    print(Encryption.xor('ceci est un message'))

    string = "Ceci est un message de test"
    print(len(string)*8)
    print(oct_to_int(to_oct_array(string)))
    print(arr_to_int(oct_to_int(to_oct_array(string))))
    print(len("{0:b}".format(arr_to_int(oct_to_int(to_oct_array(string))))))
    print(int_to_arr(arr_to_int(oct_to_int(to_oct_array(string)))))
    
    a = Thread(loop_number = 10, f = event_called, auto_init=False)
    a.begin()
    while(a.current_state != 'idle'):
        sleep(0.5)
    print("before")
    a.run_once()
    print("after")
    a.start()
    pass