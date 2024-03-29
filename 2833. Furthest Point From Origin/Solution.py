class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dt = Counter(moves)
        l = dt.get("L", 0)
        r = dt.get("R", 0)
        _ = dt.get("_", 0)
        if l >= r:
            return l + _ - r
        return r + _ - l
