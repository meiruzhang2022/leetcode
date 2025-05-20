from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        node=root
        res=[]
        while node or stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(res)
        for i in range(len(res)-1):
            if res[i]>res[i+1]:
                return False
        return True
root = TreeNode(2)
root.left = TreeNode(1)
root.right=TreeNode(3)
sol = Solution()
print(sol.isValidBST(root))