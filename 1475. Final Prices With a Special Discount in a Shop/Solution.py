class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for ind, val in enumerate(prices):
            while stack and stack[-1][1] >= val:
                prices[stack[-1][0]] = stack[-1][1] - val
                stack.pop()
            stack.append((ind,val))
          
        return prices
