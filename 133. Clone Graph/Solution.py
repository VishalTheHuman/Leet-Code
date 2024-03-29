'''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        def dfs(node):
            if node.val in visited:
                return visited[node.val]
            neighbors = []
            visited[node.val] = Node(node.val)
            for x in node.neighbors:
                neighbors.append(dfs(x))
            visited[node.val].neighbors = neighbors
            return visited[node.val]
        return dfs(node)
