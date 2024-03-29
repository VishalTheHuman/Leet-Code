import string
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)
        diff = 0
        for char in string.ascii_letters[:26]:
            diff += abs(s.get(char,0) - t.get(char,0))
        return diff//2
