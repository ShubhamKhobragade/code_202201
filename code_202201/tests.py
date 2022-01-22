import unittest
import app
from jsonRead import readRawData,checkKeysInjson

class TestBmiCalculator(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_keys(self):
        self.assertEqual(checkKeysInjson(['Gender','HeightCm','WeightKg']),'Keys Available')

    def test_bmi(self):
        self.assertEqual(app.bmiCalculator(),'Executed')
    
    def test_total_overweight_person(self):
        self.assertEqual(app.totalOverweightPerson(),'Executed')

if __name__== '__main__':
    unittest.main()