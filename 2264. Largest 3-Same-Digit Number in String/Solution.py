class Solution:
    def largestGoodInteger(self, num: str) -> str:
        val = None
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                k = num[i:i+3]
                if val is None or k > val:
                    val = k
        return "" if not val else val
