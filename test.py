import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_ping(self):
		self.assertEquals(True, True)

	def test_fail(self):
		self.assertEquals(True, False)
