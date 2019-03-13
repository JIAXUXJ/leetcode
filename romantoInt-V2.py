class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        s = s[::-1]
        last = None
        for item in s:
            if last and romanDict[item] < last:
                res -= 2*romanDict[item]
            res += romanDict[item]
            last = romanDict[item]
        return res