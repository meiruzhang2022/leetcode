from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def get_maxvalue(self,temp:List[int])->int:
        max_value=0
        index=-1
        for i in range(len(temp)):
            if temp[i]>=max_value:
                max_value=temp[i]
                index=i
        return index
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        index=self.get_maxvalue(nums)
        node=TreeNode(nums[index])
        node.left=self.constructMaximumBinaryTree(nums[:index])
        node.right=self.constructMaximumBinaryTree(nums[index+1:])
        return node
sol=Solution()
nums=[3,2,1,6,0,5]
print(sol.constructMaximumBinaryTree(nums))
