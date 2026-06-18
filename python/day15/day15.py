#Testing a class
"""Now we'll run how to test a class.
Python provides a number of assert methods in the unittest.testcase class
here are:
- assertEqual(a,b) :- it verifies that a==b
- assertNotEqual(a,b) :- it verifies that a!=b
- assertTrue(x) :- it verifies that x is True
- assertFalse(x) :- it verifies that x is False
- assertIn(item, list) :- it verifies that items is in list
- assertNotIn(item, list) :- it verifies that item is not in list

Testing a class is similar to testing a function, which is much of your work involves testing the
behavior of the methods in the class. But there are a few differences.
"""
class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print ('- ' + response)
            