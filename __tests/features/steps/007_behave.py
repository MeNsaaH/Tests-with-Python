from behave import *
from os import path
import os
from funcs import *


CWD = os.getcwd()

@given('the file "{a}" previously exists')
def step_impl(context, a):
    assert path.isfile(path.join(CWD, a)) is True

@when('the rm() function is called on the file "{a}"')
def step_impl(context, a):
    rm(path.join(CWD, a))

@then('the file "{a}" ceases to exist')
def step_impl(context, a):
    assert path.isfile(path.join(CWD, a)) is False