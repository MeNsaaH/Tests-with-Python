""" Illustration of Doctests """

def square(x):
    """ Returns square of x
    >>> square(2)
    4
    >>> square(4)
    16
    """
    return x ** 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
