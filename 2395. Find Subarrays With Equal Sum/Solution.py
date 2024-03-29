class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_set = set()
        s = sum(nums[0:2])
        sum_set.add(s)
        for j in range(len(nums)-2):
            s -= nums[j]
            s += nums[j+2]
            if s in sum_set:
                return True
            sum_set.add(s)            
        return False
