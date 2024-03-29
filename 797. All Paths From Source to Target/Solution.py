class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        end_node = len(graph)-1
        def traverse(curr_node,visited = []):
            nonlocal end_node
            if curr_node==end_node:
                paths.append(visited+[curr_node])
                return
            for node in graph[curr_node]:
                if node not in visited:
                    traverse(node,visited+[curr_node])
        traverse(0)
        return paths
