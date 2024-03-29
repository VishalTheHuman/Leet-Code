class Solution:
    def minOperations(self, s: str) -> int:
        mode_1 = "0"
        mode_2 = "1"
        count_1 = count_2 = 0
        for ch in s:
            if mode_1!=ch:
                count_1+=1
            if mode_2!=ch:
                count_2+=1
            mode_1, mode_2 = mode_2,mode_1
        return min(count_1,count_2)
