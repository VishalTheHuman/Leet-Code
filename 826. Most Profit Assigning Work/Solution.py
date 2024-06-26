class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse = True)
        value = sorted([(x,y) for x,y in zip(difficulty, profit)], reverse=True, key = lambda x : x[1])
        max_profit = idx = 0
        for w in worker:
            while idx < len(value):
                if value[idx][0] <= w:
                    max_profit += value[idx][1]
                    break
                idx += 1
        return max_profit
