class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op = nums[0]
        for x in nums[1:]:
            op ^= x
        op = bin(op)[2:]
        k = bin(k)[2:]
        fill_length = max(len(op), len(k))
        op = op.zfill(fill_length)
        k = k.zfill(fill_length)
        return sum(x!=y for x,y in zip(op,k))
