class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = [travel[0]]
        for i in range(1,len(travel)):
            prefix_sum.append(prefix_sum[i-1]+travel[i])
        time = 0
        for g in ["M","P","G"]:
            if g not in "".join(garbage):
                continue
            last_seen = -1
            for i in range(len(garbage)):
                val = garbage[i].count(g)
                if val:
                    time += val
                    garbage[i] = garbage[i].replace(g,"")
                    last_seen = i
            if last_seen>0:
                time += prefix_sum[last_seen-1]
        return time
