""" Illustration of Doctests """

def square(x):
    """ Returns square of x
    >>> square(2)
    4
    >>> square(4)
    16
    """
    return x ** 2

def my_function(a, b):
    """Returns a * b"""
    return a * b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
