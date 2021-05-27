'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from Object import *


class BaseEnum(Object):
    '''Enum Holder Class
    Holds an enum with selected features.'''
    def __new__(cls, d):
        '''New operator'''
        atts = tuple(a[:] for a in cls.__get_attributes__(cls) if a != '')
        index = [a[1] for a in atts].index(d)
        return atts[index][0]
         
    def __class_getitem__(cls, k:str):
        '''Class Getitem operator'''
        return getattr(cls, k)
