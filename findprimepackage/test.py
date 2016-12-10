import unittest
from findprime import find

class MyTest(unittest.TestCase):
	def test_valid_cases_1(self):
		self.assertListEqual(find(1,10), [2, 3, 5, 7])
	def test_valid_cases_2(self):
		self.assertListEqual(find(1,1), [])
	def test_valid_cases_3(self):
		self.assertListEqual(find(0,2), [2])
	def test_valid_cases_4(self):
		self.assertListEqual(find(-10,3), [2, 3])

	def test_error_cases_1(self):
		self.assertRaises(TypeError, find, None, None)
	def test_error_cases_2(self):
		self.assertRaises(TypeError, find, "", 3)
	def test_error_cases_3(self):
		self.assertRaises(TypeError, find, 3, "")

if __name__ == '__main__':
    unittest.main()