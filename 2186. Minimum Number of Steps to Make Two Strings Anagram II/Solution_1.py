import string
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum([abs(s.count(alphabet)-t.count(alphabet)) for alphabet in string.ascii_letters[:26]])
