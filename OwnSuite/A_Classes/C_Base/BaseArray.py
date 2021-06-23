'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from Object import *


class BaseArray(Object):
    '''Array Base Class
    Holds an array with selected features.'''
    __it    = None
    __datas = None

    def __init__(self, data:(list, tuple) = None, **kwargs):
        '''Constructor

        :param data: The list to be stored - (list, tuple) (default None)
        :kwarg **kwargs: Object parameter'''
        Object.__init__(self, **kwargs)
        if(data == None):
            data = []
        self.__datas = list(data)
        
    def __bool__(self):
        '''Bool operator'''
        false_values = [0, 0.0, False, tuple(), list(), dict(), set(), '']
        return not self.__datas in false_values

    def __len__(self):
        '''Len operator'''
        return len(self.__datas)

    def __getitem__(self, index:int):
        '''Getitem operator'''
        return self.__datas[index]

    def __setitem__(self, index:int, d):
        '''Setitem operator'''
        self.__datas[index] = d

    def __delitem__(self, index:int):
        '''Delitem operator'''
        del self.__datas[index]

    def __iter__(self):
        '''Iter operator'''
        self.__it = 0
        return self

    def __next__(self):
        '''Next operator'''
        if(self.__it == len(self)):
            raise StopIteration
        data = self.__datas[self.__it]
        self.__it += 1
        return data
 
    def __reversed__(self):
        '''Reversed operator'''
        res = []
        for self.__it in range(len(self))[::-1]:
            res.append(self.__datas[self.__it])
        return res

    def __contains__(self, d):
        '''Contains operator'''
        return d in self.__datas