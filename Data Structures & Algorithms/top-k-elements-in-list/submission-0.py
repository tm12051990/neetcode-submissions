class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq ={}
        for num in nums:
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 1

        buckets =[[] for i in range(len(nums) + 1)]

        for num, freq in numFreq.items():
            buckets[freq].append(num)

        result = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result


