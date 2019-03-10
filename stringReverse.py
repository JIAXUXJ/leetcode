import unittest
class StringMonitor(object):
	"""docstring for StringMonitor"""
	def __init__(self, s):
		super(StringMonitor, self).__init__()
		self.curStr = s

	def reverseString(self):
		"""
		:type s: str
		:rtype: str
		"""
		return (self.curStr[::-1])

class Test_StringMonitor(unittest.TestCase):
	"""docstring for Test_StringMonitor"""
	def test__init(self):
		s = StringMonitor('ab')
		self.assertEqual('ab', s.curStr)
	def test_reverse_normal(self):
		s = StringMonitor('abcd0io')
		self.assertEqual('oi0dcba', s.reverseString())
	def test_reverse_empty(self):
		s = StringMonitor('')
		self.assertEqual('', s.reverseString())
	def test_reverse_num(self):
		s = StringMonitor('123456')
		self.assertEqual('654321', s.reverseString())


def main():
	unittest.main()

if __name__ == '__main__':
	main()
		