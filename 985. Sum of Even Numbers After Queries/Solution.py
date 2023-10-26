class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ls = []
        s = 0
        for x in nums:
            if x%2==0:
                s+=x
        for val,ind in queries:
            if nums[ind]%2==0:
                s-=nums[ind]
            nums[ind]+=val
            if nums[ind]%2==0:
                s+=nums[ind]
            ls.append(s)
        return ls
