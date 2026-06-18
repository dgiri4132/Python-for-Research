import unittest

class Employee():
    def __init__(self, annual_salary,  first_name, last_name):
        self.annual_salary=int(annual_salary)
        self.first_name=first_name
        self.last_name=last_name
    
    def give_raise(self, raise_amount = 0):
        self.annual_salary+=5000
        if raise_amount:
            self.annual_salary+=int(raise_amount)
        

class TestcaseEmployee(unittest.TestCase):
    def setUp(self):
        self.employee_record=Employee(30000, "Darshan", "Giri")
        
    def test_give_default_raise(self):
        original = self.employee_record.annual_salary
        self.employee_record.give_raise()
        self.assertEqual(self.employee_record.annual_salary, original +5000)
    
    def test_give_custom_raise(self):
        original= self.employee_record.annual_salary
        self.employee_record.give_raise(5675)
        self.assertEqual(self.employee_record.annual_salary,original +10675 )

unittest.main()