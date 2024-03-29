import string
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)
        count = 0
        for alphabet in string.ascii_letters[:26]:
            val = abs(s.get(alphabet,0) - t.get(alphabet,0))
            count+=val
        return count
