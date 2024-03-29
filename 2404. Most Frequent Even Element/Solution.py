class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = [num for num in nums if num%2==0]
        dt = Counter(nums)
        max_freq = max(dt.values()) if dt else -1
        l = []
        for k,v in dt.items():
            if v==max_freq:
                l.append(k)
        return -1 if not l else min(l)
