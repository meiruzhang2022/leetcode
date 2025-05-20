from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)<=1:
            if len(nums)==0:
                return
            if len(nums)==1:
                return TreeNode(nums[0])
        else:
            root=TreeNode(nums[len(nums)//2])
            root.left=self.sortedArrayToBST(nums[:len(nums)//2])
            root.right=self.sortedArrayToBST(nums[len(nums)//2+1:len(nums)])
            return root
nums=[-10,-3,0,5,9]
sol=Solution()
print(sol.sortedArrayToBST(nums))