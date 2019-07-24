class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n == 1 or n == 2:
            return n
        pre = 2
        prepre = 1
        ret = 0
        for i in range(3, n+1):
            ret = pre + prepre
            prepre = pre
            pre = ret
        return ret