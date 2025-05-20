from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==key:
            if root.left is None and root.right is None:
                return None
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                cur=root.right
                while cur.left:
                    cur=cur.left
                cur.left=root.left
                return root.right
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        return root
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
s = Solution()
print(s.deleteNode(root,3))