import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_ping(self):
		self.assertEquals(True, True)

	def test_fail(self):
		self.assertNotEquals(True, False)

	def test_nope(self):
		self.assertNotEquals(True, False)
