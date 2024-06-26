class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        nums = list(map(lambda x : x%2, nums))
        mismatch = 0
        arr = [0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                mismatch += 1
            arr.append(mismatch)
        results = []
        for s,e in queries:
            results.append(arr[s] == arr[e])
        return results
