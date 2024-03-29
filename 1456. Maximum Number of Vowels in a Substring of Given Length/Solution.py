class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for i in range(k):
            if s[i] in "aeiou":
                count+=1
        curr_count = count
        for i in range(1,len(s)-k+1):
            if s[i-1] in "aeiou":
                curr_count-=1
            if s[i+k-1] in "aeiou":
                curr_count+=1
            count = max(count,curr_count)
        return count
