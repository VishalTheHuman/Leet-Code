class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rowSum = [(val, idx) for idx, val in enumerate(rowSum)]
        answer = [[0]*len(colSum) for _ in range(len(rowSum))]
        heapq.heapify(rowSum)
        while rowSum:
            val, idx = heapq.heappop(rowSum)
            i = 0 
            while val > 0 and i < len(colSum):
                if colSum[i]!=0:
                    diff = min(val, colSum[i])
                    val -= diff
                    colSum[i] -= diff
                    answer[idx][i] = diff
                i+=1
        return answer
