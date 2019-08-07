class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if k != i:
                    temp = nums[k]
                    nums[k] = nums[i]
                    nums[i] = temp
                    k = k+1
                else:
                    k = k+1
        