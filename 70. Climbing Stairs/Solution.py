class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        for i in range(n-2,-1,-1):
            arr[0], arr[1] = arr[0]+arr[1], arr[0]
        return arr[0]
