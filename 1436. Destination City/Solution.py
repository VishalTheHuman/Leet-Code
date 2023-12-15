class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for src,dest in paths:
            s.add(src)
        for src,dest in paths:
            if dest not in s:
                return dest
