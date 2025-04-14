from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
#回溯法
# class Solution:
#     def traversal(self,cur:TreeNode,path:List[int],res:List[str]) -> List[int]:
#
#         path.append(str(cur.val))
#         if cur.left==None and cur.right==None:
#             strings=""
#             for i in range(len(path)-1):
#                 strings+=path[i]
#                 strings+="->"
#             strings+=str(cur.val)
#             res.append(strings)
#             return
#         if cur.left:
#             self.traversal(cur.left,path,res)
#             path.pop()
#         if cur.right:
#             self.traversal(cur.right,path,res)
#             path.pop()
#     def binaryTreePaths(self, root: Optional[TreeNode])->List[str]:
#         path=[]
#         res=[]
#         if root==None:
#             return res
#         self.traversal(root, path, res)
#         return res
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode])->List[str]:
        if not root:
            return []
        stack=[(root,[str(root.val)])]
        res=[]
        while stack:
            cur,path=stack.pop()
            if cur.left is None and cur.right is None:
                res.append('->'.join(path))
            if cur.right:
                new_path=path+[str(cur.right.val)]
                stack.append((cur.right,new_path))
            if cur.left:
                new_path=path+[str(cur.left.val)]
                stack.append((cur.left,new_path))

        return res


s=Solution()
root=TreeNode(11)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
print(s.binaryTreePaths(root))