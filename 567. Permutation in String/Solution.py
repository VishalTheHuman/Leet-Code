class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # Ordinal of 'a' is 97
        w_1 = [0] * 26
        w_2 = [0] * 26
        size = len(s1)
        for x, y in zip(s1,s2[:size]):
            w_1[ord(x)-97] += 1
            w_2[ord(y)-97] += 1
        for i in range(size, len(s2)):
            if w_1 == w_2:
                return True
            w_2[ord(s2[i-size])-97] -= 1
            w_2[ord(s2[i])-97] += 1
        return w_1 == w_2
