from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSame(self,left:Optional[TreeNode],right: Optional[TreeNode])-> bool:
        if left is None and right:
            return False
        elif left and right is None:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False
        return self.isSame(left.left,right.right) and self.isSame(left.right,right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isSame(root.left,root.right)
sol=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(None)
root.left.right=TreeNode(3)
root.right.left=TreeNode(None)
root.right.right=TreeNode(3)
print(sol.isSymmetric(root))