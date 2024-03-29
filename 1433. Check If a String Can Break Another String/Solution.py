class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        possible_s1 = True
        possible_s2 = True
        for i in range(len(s1)):
            if possible_s1 or possible_s2:
                if s1[i] < s2[i]:
                    possible_s1 = False
                if s2[i] < s1[i]:
                    possible_s2 = False
            else:
                break    
        return possible_s1 or possible_s2
