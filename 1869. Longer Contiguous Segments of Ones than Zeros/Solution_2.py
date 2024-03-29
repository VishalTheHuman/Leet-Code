class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_zero = 0
        max_one = 0
        i = 0
        while i < len(s):
            count = 0
            while i < len(s) and s[i]=="1":
                i+=1
                count+=1
            max_one = max(count,max_one)
            count = 0
            while i < len(s) and s[i]=="0":
                i+=1
                count+=1
            max_zero = max(count,max_zero)
        return max_one > max_zero
