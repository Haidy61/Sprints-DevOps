target = __import__("sprints.py")
MyFunc= target.MyFunc
import unittest
import statistics
from Sprints-DevOps import MyFunc
class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [10, 20, 30]
        result =statistics.mean(data)
        self.assertEqual(result, 20)

    def test_list_fraction(self):
        data = [2.2, 3.3, 5.9]
        result = max(data)
        self.assertEqual(result, 5.9)

    def test_bad_type(self):
        data = "Haidy"
        with self.assertRaises(TypeError):
            result = MyFunc(data)
