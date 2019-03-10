import unittest
class StringMonitor(object):
	"""docstring for StringMonitor"""
	def __init__(self, s):
		super(StringMonitor, self).__init__()
		self.curStr = s

	def reverseString1(self):
		"""
		:type s: str
		:rtype: str
		# """
		# print(self.curStr[::-1])
		return (self.curStr[::-1])
	def reverseString2(self):
		"""
		Do not return anything, modify s in-place instead.
		"""
		start = 0
		newList = list(self.curStr)
		end = len(self.curStr) - 1
		while(start < end):
			newList[start],newList[end]=newList[end],newList[start]
			start+=1
			end-=1
		self.curStr = ''.join(str(i) for i in newList)
		print(self.curStr)
		return self.curStr

class Test_StringMonitor(unittest.TestCase):
	"""docstring for Test_StringMonitor"""
	def test__init(self):
		s = StringMonitor('ab')
		self.assertEqual('ab', s.curStr)
	def test_reverse_normal(self):
		s = StringMonitor('abcd0io')
		self.assertEqual('oi0dcba', s.reverseString2())
	def test_reverse_empty(self):
		s = StringMonitor('')
		self.assertEqual('', s.reverseString2())
	def test_reverse_num(self):
		s = StringMonitor('123456')
		self.assertEqual('654321', s.reverseString2())


def main():
	unittest.main()
	# s = StringMonitor('abcd')
	# s.reverseString2()

if __name__ == '__main__':
	main()
		