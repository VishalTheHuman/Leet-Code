class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        position = Counter(position)
        even = odd = 0
        for x,y in position.items():
            if x % 2 == 1:
                odd += y
            else:
                even += y
        return min(odd,even)
