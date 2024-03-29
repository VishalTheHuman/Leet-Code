class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        road_network = defaultdict(list)
        for s,d in roads:
            road_network[s].append(d)
            road_network[d].append(s)
        rank = 0
        for i in range(n):
            curr = 0
            for j in range(i+1,n):
                curr = len(road_network[i])+len(road_network[j])
                if i in road_network[j]:
                    curr-=1
                if curr > rank:
                    rank = curr
        return rank
