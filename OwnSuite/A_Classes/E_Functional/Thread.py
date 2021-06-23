'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


from threading import Thread as Th
from time import sleep

from Object import *
from StateMachine import *


class Thread(Object, Th):
    __state_machine = None
    __loop_number   = None
    __f             = None
    
    def __init__(self, loop_number:int = 0, f:callable = None, auto_init:bool = True, **kwargs):
        Object.__init__(self, **kwargs)
        Th.__init__(self)
        states_list = ('not started','startup','idle','before','loop','after','quit')
        self.__state_machine = StateMachine(states_list)
        self.__loop_number = loop_number
        self.__f = f
        if(auto_init):
            self.begin()

    @property
    def states_list(self):
        '''Property accessor

        :return: The list of states stored'''
        return self.__state_machine.states_list
            
    @property
    def current_state(self):
        '''Property accessor

        :return: The current state stored'''
        return self.__state_machine.current_state

    @current_state.setter
    def current_state(self, d:str):
        '''Property mutator

        :param d: The current state to be stored - str'''
        self.__state_machine.current_state = d
        
    @property
    def loop_number(self):
        '''Property accessor

        :return: The number of times the loop will run '''
        return self.__loop_number

    @loop_number.setter
    def loop_number(self, d:int):
        '''Property mutator

        :param d: The number of times the loop will run - int'''
        self.__loop_number = d

    def begin(self):
        '''Method
        Starts the thread at startup state.'''
        self.current_state = self.states_list[1]
        Th.start(self)

    def start(self):
        '''Method
        Starts the loop.'''
        self.current_state = self.states_list[3]

    def stop(self):
        '''Method
        Stops the loop.'''
        self.current_state = self.states_list[5]

    def end(self):
        '''Method
        Stops the loop.'''
        self.current_state = self.states_list[6]
        Th.join(self)


    def run_once(self):
        '''Method
        Runs the loop one time.'''
        tmp = self.__loop_number
        self.__loop_number = 1
        self.start()
        while(self.current_state != self.states_list[2]):
            sleep(0.1)
        self.__loop_number = tmp

    def run(self):
        '''Method
        Runs the loop.'''
        self.startup()
        self.current_state = self.states_list[2]
        while(self.current_state != self.states_list[-1]):
            if(self.current_state == self.states_list[2]):
                self.idle()
                continue
            if(self.current_state == self.states_list[3]):
                self.before()
                self.__current_loop = 0
                self.current_state = self.states_list[4]
                continue  
            if(self.current_state == self.states_list[4]):
                self.loop()
                self.__current_loop +=1
                if(self.__current_loop == self.__loop_number):
                    self.current_state = self.states_list[5]
                continue  
            if(self.current_state == self.states_list[5]):
                self.after()
                self.current_state = self.states_list[2]
                continue
        self.quit()


    def startup(self):
        '''Method
        Does nothing. 
        Can be redefined by user'''
        pass

    def idle(self): 
        '''Method
        Waits for 0.5s. 
        Can be redefined by user'''
        sleep(0.5)

    def before(self):
        '''Method
        Does nothing. 
        Can be redefined by user'''
        pass

    def loop(self): 
        '''Method
        Calls f function. 
        Can be redefined by user'''
        if(self.__f != None): 
            self.__f()

    def after(self):
        '''Method
        Does nothing. 
        Can be redefined by user'''
        pass

    def quit(self):
        '''Method
        Does nothing. 
        Can be redefined by user'''
        pass