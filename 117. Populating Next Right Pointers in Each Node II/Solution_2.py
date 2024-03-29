"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        q = [root]
        while q and root:
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(1,len(q)):
                q[i-1].next = q[i]
        return root
