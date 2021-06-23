'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from Object import *


class BaseDictionary(Object):
    '''Dictionary Base Class
    Holds a dictionary with selected features.'''
    __it    = None
    __datas = None
    __keys  = None

    def __init__(self, data:dict = None, **kwargs):
        '''Constructor

        :param data: The dict to be stored (default {})
        :kwarg **kwargs: Object parameter'''
        Object.__init__(self, **kwargs)
        if(data == None):
            data = {}
        self.__keys = list(data.keys())
        self.__datas = list(data.values())

    def __bool__(self):
        '''Bool operator'''
        false_values = [0, 0.0, False, tuple(), list(), dict(), set(), '']
        return not self.__keys in false_values

    def __len__(self):
        '''Len operator'''
        return len(self.__keys)

    def __getitem__(self, k:str):
        '''Getitem operator'''
        return self.__datas[self.__keys.index(k)]

    def __setitem__(self, k:str, d):
        '''Setitem operator'''
        self.__datas[self.__keys.index(k)] = d

    def __delitem__(self, k:str):
        '''Delitem operator'''
        index = self.__keys.index(k)
        del self.__datas[index]
        del self.__keys[index]

    def __iter__(self):
        '''Iter operator'''
        self.__it = 0
        return self

    def __next__(self):
        '''Next operator'''
        if(self.__it == len(self)): 
            raise StopIteration
        k = self.__keys[self.__it]
        self.__it += 1
        return k

    def __reversed__(self):
        '''Reversed operator'''
        res = {}
        for i in range(len(self))[::-1]:
            res[self.__keys[i]] = self.__datas[i]
        return res

    def __contains__(self, k:str):
        '''Contains operator'''
        return k in self.__keys