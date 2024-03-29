class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = [0]
        curr = 0
        for i in range(len(travel)):
            curr += travel[i]
            prefix_sum.append(curr)
        time = len("".join(garbage))
        m = 0
        p = 0
        g = 0
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                m = i
            if "G" in garbage[i]:
                g = i
            if "P" in garbage[i]:
                p = i
        time += prefix_sum[m]
        time += prefix_sum[g]
        time += prefix_sum[p]
        return time
