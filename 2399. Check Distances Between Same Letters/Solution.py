class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dt = {}
        for i in range(len(s)):
            dt[s[i]] = dt.get(s[i],[]) + [i]
        for k,v in dt.items():
            if abs(v[0]-v[1])-1 != distance[ord(k)-ord('a')]:
                return False
        return True
