class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = set()
        for s,d in edges:
            g.add(d)
        result = []
        for i in range(n):
            if i not in g:
                result.append(i)
        return result[0] if len(result)==1 else -1
