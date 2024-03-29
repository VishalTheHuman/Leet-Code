class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dt = Counter(text)
        count = len(text)
        for ch in "ban":
            if ch not in dt:
                return 0
            count = min(count,dt[ch])
        for ch in "lo":
            if ch not in dt:
                return 0
            count = min(count,dt[ch]//2)
        return count
