class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for idx, val in enumerate(nums):
            for idx2, val2 in enumerate(nums[idx+1:], start=idx+1):
                if (val + val2 == target):
                    return [idx, idx2]
                    