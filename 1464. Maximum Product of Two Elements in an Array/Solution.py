class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        n1, n2 = heapq.nlargest(2,nums)
        return (n1-1)*(n2-1)
