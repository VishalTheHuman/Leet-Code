class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        curr = str(num)
        count = 0
        for i in range(len(curr)-k+1):
            val = int(curr[i:i+k])
            if val and num % val  == 0 : 
                count += 1
        return count
