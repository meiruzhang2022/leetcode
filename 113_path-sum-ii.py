from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        if root is None:
            return res
        stack=[(root,root.val,[root.val])]
        while stack:
            node,sum_path,path=stack.pop()
            if sum_path==targetSum and node.left is None and node.right is None:
                res.append(path)
                continue
            if node.left:
                left_path=path+[node.left.val]
                stack.append([node.left,sum_path+node.left.val,left_path])
            if node.right:
                right_path=path+[node.right.val]
                stack.append([node.right,sum_path+node.right.val,right_path])
        return res
    def traverse(self,node:TreeNode,sum,path:List[int],res:List[List[int]],targeSum):
        if sum==targeSum and node.left is None and node.right is None:
            res.append(path)
        if node.left:
            self.traverse(node.left,sum+node.left.val,path+[node.left.val],res,targeSum)
        if node.right:
            self.traverse(node.right, sum+node.right.val, path+[node.right.val],res,targeSum)
        return res
    def pathSum1(self, root: Optional[TreeNode], targetSum: int):
        res=[]
        if root is None:
            return res
        sum=root.val
        path=[root.val]
        return self.traverse(root,sum,path,res,targetSum)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
sol = Solution()
print(sol.pathSum(root,targetSum=22))
print(sol.pathSum1(root,targetSum=22))