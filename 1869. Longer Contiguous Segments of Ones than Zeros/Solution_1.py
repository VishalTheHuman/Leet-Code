class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_zero = 0
        max_one = 0
        curr_zero = 0
        curr_one = 0
        for i in s:
            if i=="1":
                curr_one+=1
                curr_zero=0
                max_one = max(max_one,curr_one)
            else:
                curr_zero+=1
                curr_one=0
                max_zero = max(max_zero,curr_zero)
        return max_one > max_zero
