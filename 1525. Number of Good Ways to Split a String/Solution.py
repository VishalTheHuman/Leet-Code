class Solution:
    def numSplits(self, s: str) -> int:
        d1 = Counter(s)
        d1_len = len(d1)
        d2 = set()
        d2_len = 0
        count = 0
        for i in range(1, len(s)):
            if d1[s[i-1]] == 1:
                d1_len -=1
            else:
                d1[s[i-1]] -= 1
            if s[i-1] not in d2:
                d2.add(s[i-1])
                d2_len += 1
            count += (d1_len == d2_len)
        return count
