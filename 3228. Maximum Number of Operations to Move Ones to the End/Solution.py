class Solution:
    def maxOperations(self, s: str) -> int:

        ones = [idx for idx in range(len(s)) if s[idx]=="1"]
        count = 0
        
        for i in range(len(ones)-1):
            if ones[i+1] - ones[i] != 1:
                count += (i+1)
        
        if s[-1] == "0":
            count += len(ones)

        return count
