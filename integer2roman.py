class Solution:
    def intToRoman(self, num: int) -> str:
        num_range = [1000, 900, 500, 400,
		100, 90, 50, 40,
		10, 9, 5, 4,
		1]
        # romanDict = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        roman_range = ["M", "CM", "D", "CD",
		"C", "XC", "L", "XL",
		"X", "IX", "V", "IV",
		"I"]
        res = ''
        i = 0
        count = 0
        while num > 0:
            count = num // num_range[i]
            num %= num_range[i]
            while count > 0:
                res += roman_range[i]
                count -= 1
            i += 1
        return res
            
                