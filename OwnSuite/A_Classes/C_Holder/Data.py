'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from BaseData import *


class Data(BaseData):
    '''Data Holder Class
    Holds a data with selected features.
    
    Events are called when data.setter is called.'''
    __data = None
    
    def __init__(self, data = 0, **kwargs):
        '''Constructor

        :param data: The data to be stored (default 0)
        :kwarg **kwargs: Object parameter'''
        BaseData.__init__(self, data, **kwargs)
        self.__data = self._BaseData__data
        
    @property
    def data(self):
        '''Property accessor

        :return: The data stored'''
        return self.__data

    @data.setter
    @call_event
    def data(self, d):
        '''Property Mutator

        :param d: The data to be stored'''
        self.__data = d