class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inEdges = [0]*(n+1)
        outEdges = [0]*(n+1)
        for k,v in trust:
            outEdges[k]+=1
            inEdges[v]+=1
        for i in range(1,n+1):
            if inEdges[i]==n-1 and outEdges[i]==0:
                return i
        return -1
