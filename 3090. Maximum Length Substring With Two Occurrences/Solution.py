class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 2
        freq = defaultdict(int)
        for i in range(len(s)):
            freq.clear()
            freq[s[i]] = 1
            curr = 1
            for j in range(i+1, len(s)):
                if freq[s[j]] == 2:
                    max_len = max(max_len, curr)
                    break
                curr += 1
                freq[s[j]] += 1
            max_len = max(max_len, curr)
        return max_len
