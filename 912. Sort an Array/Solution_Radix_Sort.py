class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        buffer = 0
        if min(nums) < 0:
            buffer = -1*(min(nums))
            nums = [x+buffer for x in nums]
        
        for i in range(int(math.log(max(nums),10)+1)):
            count = [0]*10
            for x in nums:
                x//=(10**(i))
                x%=10
                count[x]+=1
            for j in range(1,10):
                count[j]+=count[j-1]
            newArr = [0]*len(nums)
            for x in nums[::-1]:
                elem = x
                x//=(10**(i))
                x%=10
                count[x]-=1
                newArr[count[x]] = elem
            nums = newArr
        if buffer:
            nums = [x-buffer for x in nums]
        return nums
