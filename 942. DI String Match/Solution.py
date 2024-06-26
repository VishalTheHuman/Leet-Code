class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        minimum = 0
        maximum = len(s)
        perm = []
        for x in s:
            if x == "I":
                perm.append(minimum)
                minimum += 1
            else:
                perm.append(maximum)
                maximum -= 1
        perm.append(maximum)
        return perm
