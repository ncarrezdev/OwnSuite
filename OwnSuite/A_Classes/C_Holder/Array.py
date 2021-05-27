'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from BaseArray import *


class Array(BaseArray):
    '''Array Holder Class
    Holds an array with selected features.
    
    Events are called when {...} are called.
    - datas.setter 
    - __setitem__ 
    - append
    - insert
    - update'''
    __it    = None
    __datas = None

    def __init__(self, data:(list, tuple) = None, **kwargs):
        '''Constructor

        :param data: The list to be stored (default None)
        :kwarg **kwargs: Object parameter'''
        BaseArray.__init__(self, data, **kwargs)
        self.__datas = self._BaseArray__datas
        self.__it = self._BaseArray__it

    @property
    def datas(self):
        '''Property accessor

        :return: The data stored'''
        return self.__datas

    @datas.setter
    @call_event
    def datas(self, d:(list, tuple)):
        '''Property Mutator

        :param d: The data to be stored'''
        self.__datas = list(d)

    @call_event
    def append(self, data):
        '''Method
        Appends data to datas.
        
        :param data: The data to append'''
        self.__datas.append(data)

    @call_event
    def insert(self, index:int, data):
        '''Method
        Inserts data at index.
        
        :param index: The index of the data to insert - int
        :param data: The data to insert'''
        self.__datas.insert(index, data)

    @call_event
    def update(self, index:int, data):
        '''Method
        Updates data at index.
        
        :param index: The index of the data to update - int
        :param data: The data to update'''
        self.__datas[index] = data

    def delete(self, index:int):
        '''Method
        Deletes data at index.
        
        :param index: The index to delete - int'''
        del self.__datas[index]