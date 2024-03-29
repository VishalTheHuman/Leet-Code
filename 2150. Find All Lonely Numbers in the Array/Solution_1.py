class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dt = Counter(nums)
        l = []
        for num in nums:
            if dt[num]==1:
                if not dt.get(num-1) and not dt.get(num+1):
                    l.append(num)
        return l
