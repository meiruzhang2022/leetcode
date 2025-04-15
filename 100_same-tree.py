from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack=[p,q]
        while stack:
            cur_q=stack.pop()
            cur_p=stack.pop()
            if cur_q is None and cur_p is None:
                continue
            if cur_q is None or cur_p is None or cur_q.val != cur_p.val:
                return False
            stack.append(cur_p.left)
            stack.append(cur_q.left)
            stack.append(cur_p.right)
            stack.append(cur_q.right)
        return True
s1 = Solution1()
p=TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q=TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print(s1.isSameTree(p,q))
s2 = Solution2()
print(s2.isSameTree(p,q))
