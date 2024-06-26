class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x, y in points:
            distance = (x**2) + (y**2)
            heapq.heappush(q, (distance, (x,y)))
        return [heapq.heappop(q)[1] for _ in range(k)]
