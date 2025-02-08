from main import *
# Python is great because it has libraries for *everything*. Here's an
# example library to help us run tests!
import unittest

# Add your tests as new methods here! We've added some examples, but
# we'll grade with other, more complicated test cases. You *MUST* add
# your own tests that more thoroughly test your implementation.

class Hw1MethodsTest(unittest.TestCase):
    def setUp(self):
        # Load the student's solution
        file_path = 'main.py'  # replace with the actual filename if needed
        spec = importlib.util.spec_from_file_location("main", file_path)
        student_solution = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_solution)
        self.student_solution = student_solution
        
    def test_myname(self):
        self.assertTrue(isinstance(myName(), str))

    def test_mymax(self):
        self.assertTrue(myMax(6,3) == 6)
        self.assertTrue(myMax("abc", "def") == "def")
        self.assertTrue(myMax(24,24) == "Equal")

    def test_factorial(self):
        self.assertTrue(factorial(4) == 4 * 3 * 2 * 1)

    def test_combineand(self):
        self.assertTrue(combineAnd("abc", "xyx") == "abc and xyz")

    def test_changextoy(self):
        self.assertTrue(changeXtoY("hello world", "world", "GW") == "hello GW")

    def test_returnnexttolast(self):
        self.assertTrue(returnNextToLast([1, 2, 3, 4]) == 3)

    def test_returnsecondhalf(self):
        self.assertTrue(returnSecondHalf([1, 2, 3, 4]) == [3, 4])

    def test_addapple(self):
        self.assertTrue(addApple(["cat", "carrot"]) == ["cat", "carrot", "apple"])

    def test_myfavfoods(self):
        self.assertTrue(len(myFavFoods()) == 3)
        self.assertTrue(isinstance(myFavFoods(), list))

    def test_myfavfoodstuple(self):
        self.assertTrue(isinstance(myFavFoodsTuple(), tuple))
        self.assertTrue(len(myFavFoodsTuple()) == 3)

    def test_coursedict(self):
        self.assertTrue(courseDict()["number"] == 2541)

    def test_favfoodsmenu(self):
        self.assertTrue(isinstance(favFoodsMenu()[myFavFoods()[0]], int))

if __name__ == '__main__':
    unittest.main()
