class Solution:
    def minPartitions(self, n: str) -> int:
        n = list(map(int, list(n)))
        count = 0 
        while True:
            changes = 0
            for i in range(len(n)):
                if n[i]:
                    changes += 1
                    n[i] -= 1
            if changes:
                count+=1
            else:
                break
        return count
