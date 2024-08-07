class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n==k:
            return 0
        n = bin(n)[2:]
        k = bin(k)[2:]
        n = list(n.zfill(max(len(n), len(k))))
        k = list(k.zfill(max(len(n), len(k))))
        changes = 0
        for i in range(len(n)):
            if n[i]!=k[i] and n[i]=="1":
                n[i] = "0"
                changes +=1
        return changes if changes > 0 and n==k else -1
