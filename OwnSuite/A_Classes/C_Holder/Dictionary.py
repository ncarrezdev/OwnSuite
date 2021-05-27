'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from BaseDictionary import *


class Dictionary(BaseDictionary):
    '''Dictionary Holder Class
    Holds a dictionary with selected features.
    
    Events are called when {...} are called.
    - keys.setter
    - datas.setter 
    - dict.setter
    - __setitem__ 
    - append
    - insert
    - update'''
    __it    = None
    __datas = None
    __keys  = None

    def __init__(self, data:dict = None, **kwargs):
        '''Constructor

        :param data: The dict to be stored (default {})
        :kwarg **kwargs: Object parameter'''
        BaseDictionary.__init__(self, data, **kwargs)
        self.__datas = self._BaseDictionary__datas
        self.__keys = self._BaseDictionary__keys
        self.__it = self._BaseDictionary__it

    @property
    def keys(self):
        '''Property accessor

        :return: The keys stored'''
        return self.__keys
        
    @keys.setter
    @call_event
    def keys(self, v:(list, tuple)):
        '''Property mutator

        :param v: The keys to be stored - list, tuple'''
        if(len(v) != len(self) or
           len(v) != len(set(v))
            ):
            raise AssertionError
        self.__keys = list(v)

    @property
    def datas(self):
        '''Property accessor

        :return: The datas stored'''
        return self.__datas
        
    @datas.setter
    @call_event
    def datas(self, d:(list, tuple)):
        '''Property mutator

        :param d: The datas to be stored - list, tuple'''
        if(len(d) != len(self)):
            raise AssertionError
        self.__datas = list(d)

    @property
    def dict(self):
        '''Property accessor

        :return: The datas stored in dict form'''
        res = {}
        for i in range(len(self)):
            res[self.__keys[i]] = self.__datas[i]
        return res

    @dict.setter
    @call_event
    def dict(self, d:dict):
        '''Property mutator

        :param d: The dict to be stored - dict'''
        self.__keys = list(d.keys())
        self.__datas = list(d.values())

    @call_event
    def append(self, k:str, d):
        '''Method
        Appends a key data set.
        
        :param k: The key to append
        :param d: The data to append'''
        if(k in self.__keys):
            raise AssertionError
        self.__keys.append(k)
        self.__datas.append(d)

    @call_event
    def insert(self, index:int, k:str, d):
        '''Method
        Insert at index a key data set.
        
        :param index: The index of the data to insert - int
        :param k: The key to append
        :param d: The data to append'''
        if(k in self.__keys):
            raise AssertionError
        self.__keys.insert(index, k)
        self.__datas.insert(index, d)

    @call_event
    def update(self, k:str, d):
        '''Method
        Updates the data associated to the key.
        
        :param index: The key to update 
        :param data: The data to update'''
        self.__datas[self.__keys.index(k)] = d

    def delete(self, k:str):
        '''Method
        Deletes the given key.
        
        :param k: The key to delete'''
        del self[k]

    def at(self, index:int):
        '''Method
        Get the key data set at index.
        
        :param index: The index of the set to return - int'''
        return {self.__keys[index]:self.__datas[index]}