class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        max_profit = 0
        for p in prices:
            curr_min = min(p,curr_min)
            max_profit = max(max_profit,p-curr_min)
        return max_profit
