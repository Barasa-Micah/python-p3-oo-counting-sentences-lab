#!/usr/bin/env python3

class MyString():
    def __init__(self,value):
        if not isinstance(value,str):
            raise ValueError('The vaue must be a string.')
        
        self._value = value


        @property
        def value(self):
            return self._value
        
        @value.setter
        def value(self, new_value):
            if not isinstance(new_value,str):
                raise ValueError('The value must be a string.')
            
            self._value = new_value