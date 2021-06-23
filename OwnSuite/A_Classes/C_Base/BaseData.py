'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from Object import *


class BaseData(Object):
    '''Data Base Class
    Holds a data with selected features.'''
    __data = None

    def __init__(self, data = 0, **kwargs):
        '''Constructor

        :param data: The data to be stored (default 0)
        :kwarg **kwargs: Object parameter'''
        Object.__init__(self, **kwargs)
        self.__data = data

    def __bool__(self):
        '''Bool operator'''
        false_values = [0, 0.0, False, tuple(), list(), dict(), set(), '']
        return not self.__data in false_values