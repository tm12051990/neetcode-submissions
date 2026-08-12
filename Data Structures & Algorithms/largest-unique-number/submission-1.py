class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1


        largest = -1
        for i in count:
            if count[i] == 1:
                largest = max(largest, i)
        return largest
