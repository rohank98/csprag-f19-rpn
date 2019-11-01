import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_sub(self):
                result = rpn.calculate("3 1 -")
                self.assertEqual(2, result)
	def test_mul(self):
		result = rpn.calculate('4 8 *')
		self.assertEqual(32, result)
	def test_bad(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +")
