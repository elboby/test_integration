import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_ping(self):
		self.assertEquals(True, True)

	def test_ping2(self):
		self.assertEquals(True, True)
