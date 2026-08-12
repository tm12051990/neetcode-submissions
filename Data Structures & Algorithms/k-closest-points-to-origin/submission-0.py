class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = x*x + y*y
            heap.append((distance, point))
        heapq.heapify(heap)

        res = []

        while k > 0:
            distance, point = heapq.heappop(heap)
            res.append(point)
            k -= 1
        return res
