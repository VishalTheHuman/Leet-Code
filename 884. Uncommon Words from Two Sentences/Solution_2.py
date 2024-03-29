class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        s = set(s1+s2)
        result = []
        for word in s:
            c1 = s1.count(word)
            c2 = s2.count(word)
            if (c1 == 1 and c2 == 0) or (c1==0 and c2==1):
                result.append(word)
        return result
