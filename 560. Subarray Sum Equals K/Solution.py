class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        store = defaultdict(int)
        store[0] = 1
        nums.insert(0,0)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i]-k in store:
                count += store[nums[i]-k]
            store[nums[i]]+=1
        
        return count
