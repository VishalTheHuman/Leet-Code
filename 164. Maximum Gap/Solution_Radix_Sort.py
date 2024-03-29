class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        diff = 0
        for i in range(int(math.log(max(nums),10))+1):
            count = [0]*10
            for x in nums:
                x//= 10**(i)
                count[x%10]+=1
            for j in range(1,10):
                count[j]+=count[j-1]
            newArr = len(nums)*[0]
            for x in nums[::-1]:
                elem = x
                x//=(10**i)
                count[x%10]-=1
                newArr[count[x%10]] = elem
            nums = newArr
        for j in range(1,len(nums)):
            diff = max(diff,nums[j]-nums[j-1])
        return diff
