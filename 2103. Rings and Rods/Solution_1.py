class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0 
        dt = {}
        i = 0
        while i+1 < len(rings):
            color = rings[i]
            rod = rings[i+1]
            if not dt.get(rod,False):
                dt[rod] = color
                i+=2
                continue
            if color not in dt[rod]:
                dt[rod] +=color
                if len(dt[rod])==3:
                    count+=1
            i+=2
        return count
