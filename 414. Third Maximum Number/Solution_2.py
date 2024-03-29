class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        max_nums = sorted(nums[:3], reverse=True)
        for i in range(3,len(nums)):
            if nums[i] > max_nums[0]:
                max_nums[2], max_nums[1] = max_nums[1], max_nums[0]
                max_nums[0] = nums[i]
            elif nums[i] > max_nums[1]:
                max_nums[2] = max_nums[1]
                max_nums[1] = nums[i]
            elif nums[i] > max_nums[2]:
                max_nums[2] = nums[i]
        return max_nums[2]
