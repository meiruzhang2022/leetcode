from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack=[(root,root.val)]
        while stack:
            cur,count=stack.pop()
            cur_val=cur.val
            if count==targetSum:
                return True
            if cur.right:
                stack.append((cur.right,count+cur.right.val))
            if cur.left:
                stack.append((cur.left, count+cur.left.val))
        return False
class Solution2:
    def dfs(self, node: Optional[TreeNode],count:int,targetSum:int)->bool:
        if count==targetSum and node.left==None and node.right==None:
            return True
        if node.left and self.dfs(node.left,count+node.left.val, targetSum):
            return True
        if node.right and self.dfs(node.right,count+node.right.val,targetSum):
            return True
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        count=root.val
        return self.dfs(root,count,targetSum)

# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right=TreeNode(8)
# root.left.left = TreeNode(11)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.left.left.left = TreeNode(7)
# root.left.left.right=TreeNode(2)
# root.right.right.right = TreeNode(1)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution1()
print(s.hasPathSum(root,targetSum=5))
s = Solution2()
print(s.hasPathSum(root,targetSum=5))