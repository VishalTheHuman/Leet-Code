class Solution:
    def totalMoney(self, n: int) -> int:
        floor = n//7
        return (7*4 *floor) + sum(i*7 for i in range(1,floor)) + sum(floor+i for i in range(1,(n%7)+1))
