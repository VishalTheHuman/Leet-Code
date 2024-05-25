class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums =[k for k,v in Counter(nums).items() if v == 2]
        if nums:
            num = nums[0]
            for x in nums[1:]:
                num^=x
            return num
        return 0
