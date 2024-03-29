class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        max_profit = 0
        for p in prices:
            if p < curr_min:
                curr_min = p
            profit = p-curr_min
            if profit > max_profit:
                max_profit = profit
        return max_profit
