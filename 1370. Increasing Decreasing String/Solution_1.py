class Solution:
    def sortString(self, s: str) -> str:
        dt = Counter(s)
        string = ""
        sorted_char = sorted(dt.keys())
        while dt:
            for x in sorted_char:
                if dt[x] is not None and dt[x]==0:
                    del dt[x]
                else:
                    string+=x
                    dt[x]-=1
            sorted_char = sorted_char[::-1]
        return string
