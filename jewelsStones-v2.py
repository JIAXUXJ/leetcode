class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # J_ = list(J)
        # S_ = list(S)
        count = 0
        for i in J:
            count += S.count(i)
        return count