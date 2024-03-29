# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ##################################
        def build(nodes, ptr = 0):
            if len(nodes) == 1:
                return TreeNode(nodes[0])
            s = set(nodes)
            while ptr < len(postorder):
                if postorder[ptr] in s:
                    break
                ptr += 1
            if ptr == len(postorder):
                return None
            for i in range(len(nodes)):
                if nodes[i] == postorder[ptr]:
                    node = TreeNode(nodes[i])
                    node.left = build(nodes[:i], ptr + 1) 
                    node.right = build(nodes[i+1:], ptr + 1)
                    return node
            return None
        ##################################
        postorder.reverse()
        return build(inorder)
