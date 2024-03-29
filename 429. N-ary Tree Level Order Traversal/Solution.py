"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        ls = []
        q = deque([root])
        while q and root:
            a = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    a.append(node.val)
                    q+=node.children
            ls.append(a)
        return ls
