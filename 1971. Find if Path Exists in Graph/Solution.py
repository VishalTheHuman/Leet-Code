class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n<=1 or source==destination:
            return True
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = {source}
        q = deque([source])
        while q:
            node = q.popleft()
            for n in graph[node]:
                if n not in visited:
                    if n==destination:
                        return True
                    visited.add(n)
                    q.append(n)
        return False
