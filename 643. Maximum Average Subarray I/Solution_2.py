class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_avg = max_avg = sum(nums[i] for i in range(k))/k
        index = 0
        for i in range(k,len(nums)):
            curr_avg = curr_avg - nums[index]/k + nums[i]/k
            max_avg = max(max_avg, curr_avg)
            index += 1
        return max_avg
