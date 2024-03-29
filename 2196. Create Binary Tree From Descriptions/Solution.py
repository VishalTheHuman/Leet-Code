# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dt = {}
        child = set()
        for i in range(len(descriptions)):
            node = descriptions[i]
            child.add(node[1])
            if node[0] not in dt:
                dt[node[0]] = TreeNode(node[0])
            if node[1] not in dt:
                dt[node[1]] = TreeNode(node[1])
            if node[2]:
                dt[node[0]].left = dt[node[1]]
            else:
                dt[node[0]].right = dt[node[1]]
        for k in dt.keys():
            if k not in child:
                return dt[k]
