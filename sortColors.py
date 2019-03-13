class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = -1
        two_pointer = len(nums)
        i = 0
        while(i<len(nums)):
            if nums[i] is 2 and i < two_pointer:
                two_pointer -= 1
                nums[i], nums[two_pointer] = nums[two_pointer], nums[i]
            elif nums[i] is 0:
                zero_pointer += 1
                nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
                i += 1
            else:#1
                i += 1
            
            

            