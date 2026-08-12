class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            complement = target - nums[i]
            seen[complement] = i
