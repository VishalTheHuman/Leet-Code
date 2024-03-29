class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dt = defaultdict(int)
        for ch in s:
            dt[ch]+=1
        ret = ""
        for ch in order:
            if ch in dt:
                ret += dt[ch]*ch
                del dt[ch]
        for k,v in dt.items():
            ret+= k*v
        return ret
