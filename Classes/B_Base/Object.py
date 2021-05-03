'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from CustomClass import CustomClass
from Event import call_event


class Object(metaclass=CustomClass):
    '''BaseClass
    Handles the creation of a custom Class with custom features'''
    def __init__(self, *args, **kwargs):
        base = getattr(self, '__base__', [])
        for c in base[1:] :
            c.__init__(self, **kwargs)
        self.__data = 0

    def __repr__(self):
        '''Representation'''
        res = ''
        for attribute in dir(self):
            if (not ('__' in attribute) and not callable(getattr(self, attribute))):
                res += str(attribute) + ':' + str(getattr(self, attribute))
                res += "; "
        res = res[:-2]
        return res