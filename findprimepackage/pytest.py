import py.test
from findprime import find

def test_error_cases_1():
	py.test.raises(TypeError, find, None, None)
def test_error_cases_2():
	py.test.raises(TypeError, find, "", 3)
def test_error_cases_3():
	py.test.raises(TypeError, find, 3, "")

def test_valid_cases_1():
	assert find(1,10) == [2, 3, 5, 7]
def test_valid_cases_2():
	assert find(1,1) == []
def test_valid_cases_3():
	assert find(0,2) == [2]
def test_valid_cases_4():
	assert find(-10,3) == [2, 3]
