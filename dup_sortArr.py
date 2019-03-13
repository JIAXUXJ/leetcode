# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         index = 1
#         for i in range(len(nums)):
#             if i+1 < len(nums) and nums[i+1] != nums[i]:
#                 nums[index] = nums[i+1]
#                 index += 1
#         nums = nums[:index]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i+1] != nums[i]:
                nums[index] = nums[i+1]
                index += 1
        print(nums[:index])
        nums = nums[:index]
        return len(nums)