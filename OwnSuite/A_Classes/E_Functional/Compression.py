'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


def to_oct_array(string):
    res = []
    for c in string:
        res.append(f'{ord(c):08b}')
    return res

def arr_to_int(int_array):
    res = 0
    for i in range(len(int_array)):
        res *= 10
        if(int_array[i] in range(0,2) or 
           int_array[i] in range(10,16)):
            res *= 10
        res += int_array[i]
    return res

def int_to_arr(integer):
    integer = str(integer)
    res = []
    i = 0
    while(i < len(integer)):
        v = int(integer[i])
        if(v == 1):
            i += 1
            v *= 10
            v += int(integer[i])
        if(v == 0):
            i += 1
            v += int(integer[i])
        res.append(v)
        i += 1
    return res

def oct_to_int(oct_array):
    res = []
    for oct in oct_array:
        res.append(int(oct[:4],2))
        res.append(int(oct[4:],2))
    return res

def int_to_oct(int_array):
    res = []
    for oct in int_array:
        res.append(int(oct[:4],2))
        res.append(int(oct[4:],2))
    return res

class Compression():pass
        