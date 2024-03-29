class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            remain = len(s)%k
            arr = [s[i:i+k] for i in range(0, len(s)-remain,k)]
            if remain:
                arr.append(s[-remain:])
            for i in range(len(arr)):
                arr[i] = str(sum(ord(x)-ord("0") for x in arr[i]))
            s = "".join(arr)
        return s
