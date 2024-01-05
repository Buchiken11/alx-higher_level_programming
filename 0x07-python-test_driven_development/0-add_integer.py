#!/usr/bin/python3

    '''
    Addition of two arguments Module
    '''
    def add_integer(a, b=98):
        '''
        this fuction adds two arguments together either int or float
        Args:
            a = integer or floats
            b = integer or floats

        Raises:
            TypeError: if not integer or Float

        Returns:
            sum of the integers or if float, casted to int
        '''
        if (not isinstance(a, int) and not isinstance(a, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, int and not isinstance(b, float))
            raise TypeError("b must be an integer")
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)

        return a + b
