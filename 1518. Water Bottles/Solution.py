class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        curr = numBottles
        while numBottles >= numExchange:
            to_add = numBottles//numExchange
            numBottles = (numBottles%numExchange) + to_add
            curr += to_add
        return curr
