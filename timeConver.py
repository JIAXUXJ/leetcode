#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
	#
	# Write your code here.
	#
	endAm = re.search("AM$", s)
	startS = re.search("^12", s)
	res = s.rstrip("[AP]M")
    
	if endAm and not startS:
		return res
	elif endAm and startS:
		res = "00" + (res[2:])
	else:
		res = "%02d" % (int(res[:2])+12) + (res[2:])
	return res
if __name__ == '__main__':

	f = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	result = timeConversion(s)

	f.write(result + '\n')

	f.close()

