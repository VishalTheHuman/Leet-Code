# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.s = set()
        def recover(root,val):
            self.s.add(val)
            if root.left:
                recover(root.left,2*val+1)
            if root.right:
                recover(root.right,2*val+2)
        recover(root,0)

    def find(self, target: int) -> bool:
        return target in self.s
    int


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)