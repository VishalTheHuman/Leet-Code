class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x : x[1], reverse = True)
        units = 0
        for x, y in boxTypes:
            if (truckSize - x) >= 0:
                units += (x*y)
                truckSize -= x
            else:
                units += (truckSize*y)
                break
        return units
