from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.pre=None
    def preorder(self,node:Optional[TreeNode],res:List[List[int]])->List[List[int]]:
        if node is None:
            return res
        self.preorder(node.left,res)
        if self.pre is None:
            res.append([node.val,1])
            self.pre=node
        else:
            if self.pre.val==node.val:
                res[-1][-1]+=1
            else:
                res.append([node.val,1])
                self.pre=node
        self.preorder(node.right,res)
        return res
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        res=self.preorder(root,res)
        mode=0
        ans=[]
        for i in range(len(res)):
            if res[i][-1] == mode:
                ans.append(res[i][0])
            if res[i][-1]>mode:
                ans=[]
                mode=res[i][-1]
                ans.append(res[i][0])

        return ans
node=TreeNode(1)
node.right=TreeNode(2)
s=Solution()
print(s.findMode(node))