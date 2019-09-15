class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_dup_list = []
        for i in nums:
            if i not in no_dup_list:
                no_dup_list.append(i)
            else:
                no_dup_list.remove(i)
        return no_dup_list.pop()