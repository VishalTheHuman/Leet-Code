"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root) -> List[int]:
        if not root:
            return []
        elements = [root.val]
        for child in root.children:
            elements += self.preorder(child)
        return elements
