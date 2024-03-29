class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0]*len(edges)
        for e,s in enumerate(edges):
            scores[s]+=e
        max_score = 0
        index = 0
        for e,s in enumerate(scores):
            if s > max_score:
                max_score = s
                index = e
        return index
