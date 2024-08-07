class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def solve(node, distance = 0):
            neigh = []
            for i in range(node+1,len(paths[node])):
                if paths[node][i]:
                    neigh.append(i)
            answer[node] = distance
            distance += 1
            for x in neigh:
                if answer[x] > distance:
                    solve(x, distance)

        paths = [[0]*n for _ in range(n)]
        answer = [i for i in range(n)]
        result = []

        for i in range(n-1):
            paths[i][i+1] = 1

        for u,v in queries:
            paths[u][v] = 1
            solve(u, answer[u])
            result.append(answer[-1])

        return result
