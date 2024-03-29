# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = [root]

    def insert(self, val: int) -> int:
        if self.root is None:
            self.root = TreeNode(val)
            self.q = [self.root]
            return 0
        while self.q and self.root:
            for _ in range(len(self.q)):
                node = self.q[0]
                if node.left:
                    self.q.append(node.left)
                else:
                    node.left = TreeNode(val)
                    return node.val
                if node.right:
                    self.q.append(node.right)
                else:
                    node.right = TreeNode(val)
                    return node.val
                self.q.pop(0)

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
