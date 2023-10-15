class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        s = set()
        while len(nums):
            val = nums.pop()
            if len(s) == k :
                return count
            if val <=k :
                s.add(val)
            count+=1
        return count
