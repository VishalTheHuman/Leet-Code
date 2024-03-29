class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dt = Counter(nums)
        return [num for num in nums if dt[num]==1 and (False if dt.get(num-1) else True) and (False if dt.get(num+1) else True)]
