from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#递归法
class Solution1:
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
#迭代法
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack=[root.right,root.left]
        while stack:
            left=stack.pop()
            right=stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            stack.append(right.left)
            stack.append(left.right)
            stack.append(right.right)
            stack.append(left.left)
        return True


sol1=Solution1()
sol2=Solution2()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(4)
root.right.left=TreeNode(4)
root.right.right=TreeNode(3)
print(sol1.isSymmetric(root))
print(sol2.isSymmetric(root))