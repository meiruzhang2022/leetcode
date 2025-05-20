from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def issameTree(self, node: Optional[TreeNode],subnode: Optional[TreeNode]) -> bool:
        if node is None and subnode is None:
            return True
        if node is None or subnode is None or node.val != subnode.val:
            return False
        return self.issameTree(node.left, subnode.left) and self.issameTree(node.right, subnode.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if root.val == subRoot.val:
            return self.issameTree(root.left, subRoot.left) and self.issameTree(root.right, subRoot.right)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
<<<<<<< HEAD
=======

class Solution2:
    def issameTree(self, node: Optional[TreeNode],subnode: Optional[TreeNode]) -> bool:
        stack=[node,subnode]
        while stack:
            subnode=stack.pop()
            node=stack.pop()
            if node is None and subnode is None:
                continue
            if node is None or subnode is None or node.val != subnode.val:
                return False
            stack.append(node.left)
            stack.append(subnode.left)
            stack.append(node.right)
            stack.append(subnode.right)
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack=[root]
        while stack:
            cur=stack.pop()
            if self.issameTree(cur,subRoot):
                return True
            else:
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        return False
>>>>>>> 61eaf50 (Initial commit)
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
subRoot = TreeNode(4)
subRoot.left =TreeNode(1)
subRoot.right = TreeNode(2)
solu = Solution()
<<<<<<< HEAD
print(solu.isSubtree(root,subRoot))
=======
print(solu.isSubtree(root,subRoot))
s=Solution2()
print(s.isSubtree(root,subRoot))
>>>>>>> 61eaf50 (Initial commit)
