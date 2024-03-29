class Solution:
    def maxScore(self, s: str) -> int:
        r = l = 0
        right, left = [], []
        for i in range(len(s)):
            if s[i]=="0":
                r+=1
            if s[len(s)-1-i]=="1":
                l+=1
            right.append(r)
            left.insert(0,l)
        max_score = 0
        for i in range(1,len(s)):
            max_score = max(left[i]+right[i-1],max_score)
        return max_score
