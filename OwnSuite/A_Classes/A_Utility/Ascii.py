'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


_ascii_excludes = list(range(0,33)) + [34,39,44,47,92,96,127]
_ascii_numbers  = list(range(48,58))
_ascii_lowers   = list(range(97,123))
_ascii_uppers   = list(range(65,91))
_ascii_specials = [x for x in list(range(33,127)) 
        if not x in _ascii_excludes+_ascii_numbers+_ascii_lowers+_ascii_uppers]


class Ascii():
    '''Ascii Utility Class
    Holds global values.'''
    excludes = _ascii_excludes
    numbers  = _ascii_numbers
    lowers   = _ascii_lowers
    uppers   = _ascii_uppers
    specials = _ascii_specials