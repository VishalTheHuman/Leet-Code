"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root) -> List[int]:
        if not root:
            return []
        elements = []
        for child in root.children:
            elements+=self.postorder(child)
        elements.append(root.val)
        return elements
