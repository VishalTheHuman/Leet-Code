class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = count = 0
        prev = None
        for i in range(len(nums)):
            if nums[i] == prev and count:
                continue
            if nums[i]!=prev:
                count = 0
                nums[index] = nums[i]
                prev = nums[i]
            elif nums[i] == prev:
                nums[index] = nums[i]
                count += 1
            index+=1
        return index
