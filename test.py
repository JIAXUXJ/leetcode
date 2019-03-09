import unittest

def num_blankspace(s = ''):
	bcount = 0
	for schar in s:
		if(schar == ' '):
			bcount += 1
	return bcount

class Test_num_blankspace(unittest.TestCase):
	def test_empty(self):
		self.assertEqual(0, num_blankspace(''))
	def test_allblanks(self):
		self.assertEqual(3, num_blankspace('   '))
	def test_zeros(self):
		self.assertEqual(0, num_blankspace('abcd'))
	def test_init(self):
		self.assertEqual(4, num_blankspace(' a b c d'))

def main():
# --------------------- simple test case1 ---------------------
	print("case1: none")
	str1 = ""
	print(num_blankspace(str1))
# --------------------- simple test case2 ---------------------
	print("case2: 3 blank space without character")
	str2 = "   "
	print(num_blankspace(str2))
# --------------------- simple test case3 ---------------------
	print("case3: string without any space")
	str3 = "abcd"
	print(num_blankspace(str3))
# --------------------- simple test case4 ---------------------
	print("case4: ab cd")
	str4 = "ab cd"
	print(num_blankspace(str4))
# --------------------- simple test case5 ---------------------
	print("case5: ' ab cd '")
	str5 = " ab cd "
	print(num_blankspace(str5))
# --------------------- if within unit test -------------------
	unittest.main()

if __name__ == '__main__':
	main()