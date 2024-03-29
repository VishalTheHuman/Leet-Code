class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        dt = {score[i][k] : score[i] for i in range(len(score)) }
        ls = sorted(list(dt.keys()),reverse=True)
        return [dt[ls[i]] for i in range(len(score))]
