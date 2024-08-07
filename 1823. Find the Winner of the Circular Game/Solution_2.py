class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k==1:
            return n
        q = deque([i for i in range(n)])
        while len(q) > 1:
            for _ in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q[0]+1
