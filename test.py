import sprints as sp
def firsttestcase():
    List1 = [10,8,4,3,1,6]
    List2 = [6.1, 4.1, 8.8, 7.5, 2.3]
    result = sp.myFunc(List1, List2)
    assert result[0] == (10+8+4+6) / 4, "Should be 7"
    assert result[1] == 8.8, "Should be 8.8"
def sectestcase():
    List1 = [10,20,77,33,9,3]
    List2 = [2.1,3.6,1.9,9.9]
    result = sp.myFunc(List1, List2)
    assert result[0] == (10+20) / 2, "Should be 15"
    assert result[1] == 9.9, "Should be 9.9"
def thirdtestcase():
    List1 = ["sprints", "devops", 'haidy', 1.0, 2, 4, 7, 8]
    List2 = [ 1, 2.2, "summer",4.9,2.1]
    result = sp.myFunc(List1, List2)
    assert result[0] == (2+4+8) / 3, "Should be 4.6"
    assert result[1] == 4.9, "Should be 4.9"
if __name__ == "__main__":
    firsttestcase()
    sectestcase()
    thirdtestcase()
    print("Task 02: Tests Passed")
#target = __import__("sprints.py")
#MyFunc= target.MyFunc
#import unittest
#import statistics
#from Sprints-DevOps import MyFunc
#class TestSum(unittest.TestCase):
 #   def test_list_int(self):
  #      data = [10, 20, 30]
   #     result =statistics.mean(data)
    #    self.assertEqual(result, 20)

#    def test_list_fraction(self):
 #       data = [2.2, 3.3, 5.9]
  #      result = max(data)
  #      self.assertEqual(result, 5.9)

#    def test_bad_type(self):
 #       data = "Haidy"
  #      with self.assertRaises(TypeError):
   #         result = MyFunc(data)
