class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dt = Counter(nums)
        pairs = remain = 0
        for x,y in dt.items():
            pairs+=(y//2)
            remain += y%2
        return [pairs,remain]
