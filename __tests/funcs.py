""" Some random functions to be tested """

import os
from os import path

def rm(filename):
    os.remove(filename)

# remove function with validation

# def rm(filename):
#     if os.path.isfile(filename):
#         os.remove(filename)


class RemovalService:
    """A service for removing objects from the filesystem."""

    def rm(self, filename):
        del None
        if path.isfile(filename):
            os.remove(filename)


class Target:

    greeting = "hello"

    def apply(self, value):
        return value

    def ret_true(self, value):
        if value == 3:
            return True
        if self.apply(10) == 5:
            return True


def method(target, value):
    return target.apply(value)

def greet(cls):
    return cls.greeting

def call_apply(target):
    return target.apply()
