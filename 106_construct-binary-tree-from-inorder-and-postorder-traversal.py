from typing import List,Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        root = TreeNode()
        root.val = postorder.pop()
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index=i
                break
        left_in=inorder[:index]
        right_in=inorder[index+1:]
        left_post=postorder[:len(left_in)]
        right_post=postorder[len(left_in):len(postorder)]
        root.left=self.buildTree(left_in, left_post)
        root.right=self.buildTree(right_in, right_post)
        return root
inorder=[9,3,15,20,7]
postorder=[9,15,7,20,3]
s=Solution()
root=(s.buildTree(inorder, postorder))
print(root.val, root.left.val, root.right.val)