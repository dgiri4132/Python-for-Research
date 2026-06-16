"""
Unit test and Test Cases are used for verification of function
Unit Test verifies that one specific aspect of a function's behavior is correct.
Test case is a collection of unit tests that together prove that a function behaves as it's supposed to, within
the full rage of situations you expect it to handle. A good test case considers all the possible
kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage icnludes a full range of 
unit tests covering. all the possible ways you can use a function."""

import unittest

def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

"""
So firstly we create a class called NamesTestCase, which will contain a series of unit tests for get_formatted_name()
We make a class Test and then call unittest.TestCase as well. After that we call the method that we want to test
. The assert method helps verify that a result you received matches the result you expected to receive. It compares the 
value in formatted_name (here) to the actual output that the code produced"""