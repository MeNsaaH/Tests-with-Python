from behave import *
from funcs import my_function

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

@given('my_function exists')
def step_impl(context):
    from funcs import my_function

@then('it returns \'aaa\' when run with \'a\'')
def step_impl(context):
    ans = my_function('a', 3)
    assert ans =='aaa'