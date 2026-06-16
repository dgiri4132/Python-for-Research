#From yesterday
"""
Unit test and Test Cases are used for verification of function
Unit Test verifies that one specific aspect of a function's behavior is correct.
Test case is a collection of unit tests that together prove that a function behaves as it's supposed to, within
the full rage of situations you expect it to handle. A good test case considers all the possible
kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage icnludes a full range of 
unit tests covering. all the possible ways you can use a function.



def get_formatted_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()


So firstly we create a class called NamesTestCase, which will contain a series of unit tests for get_formatted_name()
We make a class Test and then call unittest.TestCase as well. After that we call the method that we want to test
. The assert method helps verify that a result you received matches the result you expected to receive. It compares the 
value in formatted_name (here) to the actual output that the code produced

The line unittest.main() tells the Python to run the tests in this file."""

# A Failing Test

import unittest

def get_formatted_name(first, last, middle = ''):
    if middle:
        full_name = first + ' ' + middle + ' ' +last
    else:
        full_name = first + ' ' + last
    return full_name.title()



class NamesTestClass(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()

"""Here we have many pieces of information that we can learn something from
    Firstly, The E tells us one unit test in the test case resulted in an error. After that we see
    that test_first_last_name function resulted in the error as well. 
    The third piece of information is that the traceback reports that there is a missing argument 
    the final important message is that how many trest cases failed in total.
    """

#Responding to a Failed Test

""" Given you have desinged the test properly, the thing that you can do instead of changing the test when a test case faile
is actually change the function that is causing the error. Here, instead of using first, middle and last all the time, 
we can actually use middle name only if provided one

So the function then becomes:
def get_formatted_name(first, last, middle = '')
    if middle:
        full_name = first + ' ' + middle + ' ' last
    else:
    full_name = first + ' ' + last
    return full_name.title()

    P.S. I have already changed the function above

"""