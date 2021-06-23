'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from Object import *
from Ascii  import *
from Random import *


class Encryption(Object):
    __ascii  = None

    @classmethod
    def __check_none_values__(cls):
        cls.__ascii = Ascii  
        cls.__ascii.allowed = Ascii.numbers + Ascii.lowers + Ascii.uppers + Ascii.specials

    @classmethod
    def __xor_algorithm_encryption_(cls, value):
        Encryption.__check_none_values__()
        enc = []
        key = []
        for c in value.replace(' ', '`'):
            c = ord(c) 
            k = 0
            i = 0
            max_rep = 1000
            while((k not in cls.__ascii.allowed or
                  k ^ c in cls.__ascii.excludes) and
                  i < max_rep):
                k = int(Random.random(min(cls.__ascii.allowed),max(cls.__ascii.allowed)))
                i += 1
            if(i >= max_rep):
                print('there was a problem with',chr(c))
            enc.append(k ^ c)
            key.append(k)
        return {'original' : value, 
                'encrypted':''.join([chr(c) for c in enc]), 
                'key'      :''.join([chr(k) for k in key])}

    @staticmethod
    def xor(message):
        return Encryption.__xor_algorithm_encryption_(message)