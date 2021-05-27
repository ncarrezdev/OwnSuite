'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


def call_event(f):
    '''Decorator
    Calls the method callEvent from the object
    
    The method callEvent is used only if :
    - the feature is enabled and event_auto is True
    - the feature is enabled and keyword argument force_event is True
        
    :kwarg force_event: Used to force the call - bool (default False)'''
    def decorator(*args, **kwargs):
        res = f(*args, **kwargs)
        obj = args[0]
        if(getattr(obj, 'event_list', None) != None):
            auto_call = getattr(obj, 'event_auto', False)
            force_call = kwargs.get('force_event', False)
            if(auto_call == True or force_call == True):
                obj.callEvent()
        return res
    return decorator


class Event():
    '''Features Class
    Holds a list a functions/events that can be called at any time'''
    __event_list=[]
    __event_auto=False

    def __init__(self, **kwargs):
        '''Constructor

        :kwarg event_auto: Used only in subclasses - bool (default False)'''
        self.__event_auto = kwargs.get('event_auto', False)
        self.__event_list = [] 

    @property
    def event_list(self):
        '''Property accessor

        :return: The signals list - list'''
        return self.__event_list

    @property
    def event_auto(self):
        '''Property accessor

        :return: The auto event state - bool'''
        return self.__event_auto

    @event_auto.setter
    def event_auto(self, value:bool):
        '''Property mutator

        :param value: The auto event state - bool'''
        self.__event_auto = value

    def addEvent(self, f:callable):
        '''Method
        Adds a new function/event to the existing list

        :param function: The function/event to append - callable'''
        self.__event_list.append(f)

    def delEvent(self, f:callable):
        '''Method
        Removes the function/event from the list

        :param function: The function/event to remove - callable'''
        index = self.__event_list.index(f)
        del self.__event_list[index]

    def callEvent(self):
        '''Method
        Calls all the functions/events stored in event_list'''
        for f in self.__event_list:
            f()