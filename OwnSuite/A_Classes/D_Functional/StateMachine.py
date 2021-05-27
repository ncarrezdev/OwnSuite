'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from BaseArray import *


class StateMachine(BaseArray):
    '''StateMachine Functional Class
    Manage a state machine with a states list and a current state.
    By default, sets current_state value to states_list[0].
    
    Events are called when {...} are called.
    - current_state.setter
    - prev 
    - next'''
    __it            = None
    __current_state = None
    __states_list   = None

    def __init__(self, states_list:(list, tuple) = None, **kwargs):
        '''Constructor

        :param states_list: The list of states to be stored (default None)
        :kwarg **kwargs: Object parameter'''
        BaseArray.__init__(self, states_list, **kwargs)
        self.__it          = self._BaseArray__it
        self.__states_list = self._BaseArray__datas
        if(self.__states_list):
            self.__current_state = self.__states_list[0]

    @property
    def states_list(self):
        '''Property accessor

        :return: The list of states stored'''
        return self.__states_list

    @states_list.setter
    def states_list(self, d:(list, tuple)):
        '''Property mutator

        :param d: The list of states to be stored'''
        self.__states_list = Array(d)
        if(self.__states_list):
            self.__current_state = self.__states_list[0]

    @property
    def current_state(self):
        '''Property accessor

        :return: The current state stored'''
        return self.__current_state

    @current_state.setter
    @call_event
    def current_state(self, d:str):
        '''Property mutator

        :param d: The current state to be stored'''
        if(d in self.__states_list):
            self.__current_state = d

    def __bool__(self):
        '''Bool operator'''
        false_values = [0, 0.0, False, tuple(), list(), dict(), set(), '']
        return (BaseArray.__bool__(self) and
                not self.__current_state in false_values)

    def __setitem__(self, index:int, d:str):
        '''Setitem operator'''
        BaseArray.__setitem__(self, index, d)
        if(self.__current_state not in self):
            self.__current_state = self.__states_list[0]

    def __delitem__(self, index:int):
        '''Delitem operator'''
        BaseArray.__delitem__(self, index)
        if(self.__current_state not in self):
            self.__current_state = self.__states_list[0]

    def prev(self):
        '''Method
        Set the current states to the previous on the states list.'''
        index = self.states_list.index(self.current_state)
        if(not index-1 < -len(self)):
            self.current_state = self.states_list[index-1]

    def next(self):
        '''Method
        Set the current states to the next on the states list.'''
        index = self.states_list.index(self.current_state)
        if(not index+1 > len(self)-1):
            self.current_state = self.states_list[index+1]