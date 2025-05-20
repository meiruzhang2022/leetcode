from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preoder(self,node:Optional[TreeNode],res:List[int])->List[int]:
        if node is None:
            return res
        self.preoder(node.left,res)
        res.append(node.val)
        self.preoder(node.right,res)
        return res
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=[]
        res=self.preoder(root,res)
        minimum=10**5
        for i in range(1,len(res)):
            if res[i]-res[i-1]<minimum:
                minimum=res[i]-res[i-1]
        return minimum
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left =TreeNode(1)
root.left.right = TreeNode(3)
sol = Solution()
print(sol.getMinimumDifference(root))