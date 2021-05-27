'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from CustomClass import CustomClass
from Event import call_event


class Object(metaclass=CustomClass):
    '''Base Class
    Handles the creation of a custom Class with custom features'''
    def __init__(self, *args, **kwargs):
        '''Constructor

        :arg *args: not used
        :kwarg **kwargs: Used only to enable the features in a custom class'''
        base = getattr(self, '__base__', [])
        for c in base[1:] :
            c.__init__(self, **kwargs)

    def __repr__(self):
        '''Representation operator'''
        res = ''
        res += '' + self.__class__.__name__ + '('
        for attribute, value in self.__get_attributes__():
            res += str(attribute) + ':' + \
                (str(value) if not type(value) == str else str('\''+value+'\''))
            res += "; "
        if(res != '' + self.__class__.__name__ + '('):
            res = res[:-2]
        res += ')'
        return res
        
    def __eq__(self, other):
        '''Equal operator'''
        if(other.__class__==self.__class__):
            return self.__get_attributes__() == other.__get_attributes__()
        else:
            return NotImplemented

    def __ne__(self, other):
        '''Not equal operator'''
        if(other.__class__==self.__class__):
            return self.__get_attributes__() == other.__get_attributes__()
        else:
            return NotImplemented

    def __lt__(self, other):
        '''Lesser than operator'''
        if(other.__class__==self.__class__):
            return self.__get_attributes__() < other.__get_attributes__()
        else:
            return NotImplemented

    def __le__(self, other):
        '''Lesser equal operator'''
        if(other.__class__==self.__class__):
            return self.__get_attributes__() <= other.__get_attributes__()
        else:
            return NotImplemented

    def __gt__(self, other):
        '''Greater than operator'''
        if(other.__class__==self.__class__):
            return self.__get_attributes__() > other.__get_attributes__()
        else:
            return NotImplemented

    def __ge__(self, other):
        '''Greater equal operator'''
        if(other.__class__==self.__class__):
            return self.__get_attributes__() >= other.__get_attributes__()
        else:
            return NotImplemented

    def __hash__(self):
        '''Hash operator'''
        atts = self.__get_attributes__()
        hash_map = tuple(a[:][1] for a in atts if a != '')
        return hash((self.__class__,) + hash_map)

    def __get_attributes__(self):
        '''Private Method
        Returns the list of attributes and associated values.
        
        :return: A tuple of tuple ((name, value),)'''
        res = tuple()
        for attribute in dir(self):
            if (not ('__' in attribute) and not callable(getattr(self, attribute))):
                res += ((attribute, getattr(self, attribute)),)
        return res