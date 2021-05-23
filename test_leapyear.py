import pytest
import leapyear

def leapyear_case(x):
		assert check(400) == 1
		assert check(3) == 0
		assert check(100) == 0
		assert check(16) == 1
		assert check(0) == 1
		assert check(4) == 1


