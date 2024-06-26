class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [0]*26
        upper = [0]*26
        for x in word:
            if x.islower():
                lower[ord(x)-97]+=1
            else:
                upper[ord(x)-65]+=1
        count = 0
        for i in range(26):
            if lower[i] and upper[i]:
                count += 1
        return count
