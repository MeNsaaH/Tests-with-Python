
import os
import tempfile
import unittest
from unittest import mock

import funcs


# Tests written without mocking
class RmTestCase(unittest.TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open(self.tmpfilepath, "wb") as f:
            f.write("Delete me!")

    def test_rm(self):
        # remove the file
        funcs.rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

# Our test case is pretty simple, but every time it is run, a temporary file is created and
# then deleted. Additionally, we have no way of testing whether our rm method properly
# passes the argument down to the os.remove call. We can assume that it does based on the
# test above, but much is left to be desired.


## WELCOME MOCK TESTING

# class RmTestCase(unittest.TestCase):

#     # Mock a module where it is called/used not from the base module library
#     @mock.patch('funcs.os')
#     def test_rm(self, mock_os):
#         funcs.rm("any path")
#         # test that rm called os.remove with the right parameters
#         mock_os.remove.assert_called_with("any path")


# class RmTestCase(unittest.TestCase):

#     @mock.patch('funcs.os.path')
#     @mock.patch('funcs.os')
#     def test_rm(self, mock_os, mock_path):
#         # set up the mock
#         mock_path.isfile.return_value = False

#         funcs.rm("any path")

#         # test that the remove call was NOT called.
#         self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

#         # make the file 'exist'
#         mock_path.isfile.return_value = True

#         funcs.rm("any path")

#         mock_os.remove.assert_called_with("any path")


# Mocking with Classes

# class RemovalServiceTestCase(unittest.TestCase):

#     @mock.patch('funcs.os.path')
#     @mock.patch('funcs.os')
#     def test_rm(self, mock_os, mock_path):
#         # instantiate our service
#         reference = funcs.RemovalService()

#         # set up the mock
#         mock_path.isfile.return_value = False

#         reference.rm("any path")

#         # test that the remove call was NOT called.
#         self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

#         # make the file 'exist'
#         mock_path.isfile.return_value = True

#         reference.rm("any path")

#         mock_os.remove.assert_called_with("any path")



if __name__ == '__main__':
    unittest.main()
