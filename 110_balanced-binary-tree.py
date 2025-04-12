from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#递归法
# class Solution:
#     def getdepth(self, node: TreeNode) -> int:
#         if not node:
#             return 0
#         if self.getdepth(node.left)==-1 or self.getdepth(node.right)==-1 or abs(self.getdepth(node.left)-self.getdepth(node.right))>1:
#             return -1
#         return max(self.getdepth(node.left),self.getdepth(node.right))+1
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if self.getdepth(root)==-1:
#             return False
#         return True

#迭代法:DFS
# class Solution:
#     def getdepth(self, cur: TreeNode) -> int:
#         if cur is None:
#             return 0
#         stack=[(cur,1)]
#         max_depth=0
#         while stack:
#             node, depth = stack.pop()
#             max_depth = max(max_depth, depth)
#             if node.left is not None:
#                 stack.append((node.left,depth+1))
#             if node.right is not None:
#                 stack.append((node.right,depth+1))
#         return max_depth
#     def isBalanced(self,root: TreeNode) -> bool:
#         if root is None:
#             return True
#         stack=[root]
#         while stack:
#             node = stack.pop()
#             if abs(self.getdepth(node.left)-self.getdepth(node.right))>1:
#                 print(self.getdepth(node.left),self.getdepth(node.right))
#                 return False
#             else:
#                 if node.left:
#                     stack.append(node.left)
#                 if node.right:
#                     stack.append(node.right)
#         return True
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack=[]
        node=root
        last_visited=None
        height={}
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack[-1]
                if node.right and last_visited!=node.right:
                    node=node.right
                else:
                    node=stack.pop()
                    left_height=height.get(node.left,0)
                    right_height=height.get(node.right,0)
                    if abs(left_height-right_height)>1:
                        return False
                    height[node]=max(left_height,right_height)+1
                    last_visited=node
                    node=None
        return True

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right= TreeNode(4)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(4)
root.right.left.left= TreeNode(4)
root.right.left.right= TreeNode(4)
root.left.left.left.left = TreeNode(5)
root.left.left.left.right= TreeNode(5)
print(s.isBalanced(root))