class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]

        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first == second:
                continue
            else:
                newStone = first - second
                heapq.heappush(heap, -newStone)
        if heap:
            return -heap[0]
        else:
            return 0