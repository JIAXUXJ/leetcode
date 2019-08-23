class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            if i == len(nums) - 1:
                return len(nums)