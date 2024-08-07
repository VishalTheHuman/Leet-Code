class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumArray = []
        prev = 0
        for i in range(n):
            nums[i], prev = prev+nums[i], nums[i] + prev
            sumArray.append(nums[i])
        for i in range(1,n):
            prev = nums[i-1]
            for j in range(i,n):
                sumArray.append(nums[j]-prev)
        sumArray.sort()
        answer = 0
        for idx in range(left-1, right):
            answer = (answer + sumArray[idx]) % (10**9+7)
        return answer
