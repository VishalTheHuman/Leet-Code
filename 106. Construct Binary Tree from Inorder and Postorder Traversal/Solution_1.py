# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ##################################
        def build(l,r):
            if l>=r:
                return None
            val = postorder.pop()
            right = build(builder[val]+1,r)
            left = build(l, builder[val])
            return TreeNode(val, left, right)
        ##################################
        builder = {j:i for i, j in enumerate(inorder)}
        return build(0, len(postorder))
