class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        max_val = max(nums)
        idx = curr = 0
        if 0 in nums:
            nums.remove(0)
        while max_val > curr:
            curr += (heapq.heappop(nums) - curr)
            idx += 1
        return idx
