'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from BaseArray import *


class StateMachine(BaseArray):
    __states_list   = None
    __current_state = None

    def __init__(self, states_list:(list, tuple), current_state:str = None, **kwargs):
        BaseArray.__init__(self, states_list, **kwargs)
        self.__states_list = self._BaseArray__datas
        self.__current_state = current_state
        if(self.__current_state == None):
            self.__current_state = self.__states_list[0]

    @property
    def states_list(self):
        '''Property accessor

        :return: The list of states stored'''
        return self.__states_list

    @states_list.setter
    def states_list(self, d:(list, tuple)):
        '''Property mutator

        :param d: The list of states to be stored - (list, tuple)'''
        self.__states_list = d
        if(self.__current_state not in self.__states_list):
            self.__current_state = self.__states_list[0]

    @property
    def current_state(self):
        '''Property accessor

        :return: The current state stored'''
        return self.__current_state

    @current_state.setter
    def current_state(self, d:str):
        '''Property mutator

        :param d: The current state to be stored - str'''
        if d not in self.__states_list:
            AttributeError
        self.__current_state = d
            
    def __bool__(self):
        '''Bool operator'''
        false_values = [0, 0.0, False, tuple(), list(), dict(), set(), '']
        return (bool(self.__states_list) and
                not self.__current_state in false_values)

    def prev(self):
        '''Method
        Set the current states to the previous on the states list.'''
        index = self.__states_list.index(self.__current_state)
        if(not index-1 < -len(self)):
            self.__current_state = self.__states_list[index-1]

    def next(self):
        '''Method
        Set the current states to the next on the states list.'''
        index = self.__states_list.index(self.__current_state)
        if(not index+1 > len(self)-1):
            self.__current_state = self.__states_list[index+1]
