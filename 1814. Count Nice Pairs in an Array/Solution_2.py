class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        reverse = {}
        count = 0
        for i in range(len(nums)):
            nums[i] = nums[i] - int(str(nums[i])[::-1])
        s = set(nums)
        i = 0
        for num in s:
            val = nums.count(num)
            if val > 1:
                count += sum(x for x in range(1,val))
            i+=1
        return count % (10**9 + 7)
