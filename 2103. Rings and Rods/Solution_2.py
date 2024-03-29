class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0 
        i = 0 
        color = None
        dt = {}
        while i < len(rings):
            color = rings[i]
            i+=1
            rod = rings[i]
            i+=1
            if not dt.get(rod,False):
                dt[rod] = {}
            dt[rod][color] = dt[rod].get(color,0) + 1

        for d in dt:
            if len(dt[d]) >=3:
                count+=1
        return count
