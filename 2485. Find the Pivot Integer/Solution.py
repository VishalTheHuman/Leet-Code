class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = [x+1 for x in range(n)]
        prefix = [0]*(n + 1)
        curr = 0
        for x in range(len(arr)):
            curr+=arr[x]
            prefix[x+1] = curr
        for i in range(1, len(prefix)):
            if (prefix[-1] - prefix[i]) == prefix[i-1]:
                return i
        return -1
