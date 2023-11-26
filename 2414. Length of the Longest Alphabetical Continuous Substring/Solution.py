class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        count = 1
        answer = 1
        for i in range(1,len(s)):
            if ord(s[i])-ord(s[i-1])==1:
                count +=1
                answer = max(answer,count)
            else:
                count = 1
        return answer
