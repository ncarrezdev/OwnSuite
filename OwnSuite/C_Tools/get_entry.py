'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


def get_entry(prompt, type_ = str):
    from C_Tools import valid_str_not_empty, valid_str_to_float, valid_str_to_int
    res = input(prompt)
    empty_str = lambda:valid_str_not_empty(res)
    type_foo = lambda:bool(1)
    if(type_ == int):
        type_foo = lambda:valid_str_to_int(res)
    if(type_ == float):
        type_foo = lambda:valid_str_to_float(res)
    while(not (empty_str() and type_foo())):
        if(not empty_str()):
            print('Empty String !')
        if(not type_foo()):
            print('Bad Conversion !')
        res = input(prompt)
    return type_(res)