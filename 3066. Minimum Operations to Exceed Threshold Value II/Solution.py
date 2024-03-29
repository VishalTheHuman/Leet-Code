class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while len(nums) >= 2:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >=k and y>=k:
                return count
            print(x,y)
            count += 1
            heapq.heappush(nums, min(x,y)*2 + max(x,y))
        return count
