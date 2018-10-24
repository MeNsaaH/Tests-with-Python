import unittest
from unittest import mock

from funcs import call_apply, greet, method


class MethodTestCase(unittest.TestCase):

    def test_method(self):
        target = mock.Mock()

        method(target, "value")

        target.apply.assert_called_with("value")

    # Mocking class objects

    def test_ret_value(self):
        _class = mock.Mock()
        #create a mock method apply() with a return value
        _class.apply.return_value = 5
        self.assertTrue(call_apply(_class) == 5)


# Mocking Classes and Objects

# class GreetingTestCase(unittest.TestCase):

#     def test_greeting(self):
#         _class = mock.Mock()
#         _class.greet = "hello"

#         self.assertEqual(greet(_class), 'hello')




if __name__ == '__main__':
    unittest.main()
