class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        total_happiness = 0
        for turn in range(k): 
            val = (happiness.pop() - turn)
            total_happiness += (val if val > 0 else 0)
        return total_happiness
