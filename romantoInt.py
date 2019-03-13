class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(s)):
            cur = romanDict[s[i]]
            last = 0
            if i >= 1: last = romanDict[s[i-1]]
            print(i, cur, last)
            if cur > last:
                res += cur - last*2
            else:
                res += cur
        return res