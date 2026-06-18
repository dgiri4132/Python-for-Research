import unittest
from day15 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question= "What language did you learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']




    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn( response, self.my_survey.responses)

unittest.main()

"""There is a method called setUp() in unittest.TestCase which allows you to create the objects
once and then use them in each of the test methods. The chages will ba made you to above as well.
The serUp() does two things over here, it creates a survey instance and it also
creates a list of reponses. Each of these is prefixed by self so that they can be used anywhere in the class."""