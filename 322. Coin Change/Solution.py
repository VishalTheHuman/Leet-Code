class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        coins = sorted([x for x in coins if x<=amount])

        for i in range(len(coins)):
            dp[coins[i]] = 1
        
        dp[0] = 0

        for i in range(1,amount+1):
            minimum = sys.maxsize
            for x in coins:
                if x > i:
                    break
                if dp[i-x] >= 0:
                    minimum = min(minimum, dp[i-x])
            if minimum < sys.maxsize:
                dp[i] = minimum + 1
    
        return dp[amount]
