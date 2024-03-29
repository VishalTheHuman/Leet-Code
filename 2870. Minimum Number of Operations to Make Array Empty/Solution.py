class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        operations = 0
        for k, v in count.items():
            if v < 2:
                return -1
            operations += v//3
            if v % 3 != 0:
                operations += 1
        return operations
