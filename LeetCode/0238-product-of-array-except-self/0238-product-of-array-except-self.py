class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]
        left, right = 1, 1

        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        
        return output
