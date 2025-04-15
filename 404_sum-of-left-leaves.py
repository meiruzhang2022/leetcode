from typing import Optional,List
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack=[root]
        sum=0
        while stack:
            node = stack.pop()
            if node.left:
                if node.left.left ==None and node.left.right is None:
                    sum+=node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sum
class Solution2:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftSum=0
        if root.left and root.left.left is None and root.left.right is None:
            leftSum+=root.left.val
        return leftSum+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s1 = Solution1()
print(s1.sumOfLeftLeaves(root))
s2 = Solution2()
print(s2.sumOfLeftLeaves(root))