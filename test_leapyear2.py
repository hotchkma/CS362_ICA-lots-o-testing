import leapyear
import unittest

class testCaseCalc(unittest.TestCase):
	def test_add(self):
		self.assertEqual(leapyear.check(4),1)
		self.assertEqual(leapyear.check(400),1)
		self.assertEqual(leapyear.check(3),0)
		self.assertEqual(leapyear.check(100),0)
		self.assertEqual(leapyear.check(0),1)
		self.assertEqual(leapyear.check(16),1)

if __name__ == "__main__":
	unittest.main()
