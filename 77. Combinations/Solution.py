class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        curr = []
        def combs(depth):
            if depth==0:
                result.append(curr[:])
                return
            start = curr[-1]+1 if curr else 1 
            for i in range(start, n+1):
                curr.append(i)
                combs(depth-1)
                curr.pop()
        combs(k)
        return result
