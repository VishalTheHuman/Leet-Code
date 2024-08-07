class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones = [-a, -b, -c]
        points = 0
        heapq.heapify(stones)
        while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != -1:
                heapq.heappush(stones, x+1)
            if y != -1:
                heapq.heappush(stones, y+1)
            points += 1
        return points
