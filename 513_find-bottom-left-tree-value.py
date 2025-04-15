from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        queue=deque([root])
        leftest=[]
        while queue:
            size=len(queue)
            leftest.append(queue[0])
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftest[-1].val
class Solution2:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxdepth=-1
        self.res=None
        self.dfs(root,0)
        return self.res
    def dfs(self,node,depth)->int:
        if node is None:
            return None
        if depth>self.maxdepth:
            self.maxdepth=depth
            self.res=node.val
        self.dfs(node.left,depth+1)
        self.dfs(node.right,depth+1)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left= TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
sol = Solution1()
print(sol.findBottomLeftValue(root))