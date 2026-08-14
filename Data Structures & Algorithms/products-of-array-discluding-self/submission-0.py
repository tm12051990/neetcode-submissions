class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixTotal = [1] * len(nums)
        suffixTotal = [1] * len(nums)
        result = [0] * len(nums)

        product = 1
        for i in range(len(nums)):
            prefixTotal[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffixTotal[i] = product
            product *= nums[i]

        for i in range(len(nums)):
            result[i] = prefixTotal[i] * suffixTotal[i]

        return result    


    
                
