class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        tempMax = 0

        for num in nums:
            if num == 1:
                tempMax += 1
                currentMax = max(currentMax, tempMax)
            else:
                tempMax = 0
        return currentMax


        
                