
# Definition for a Node.
from typing import Optional,List
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    #迭代法
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        if root is None:
            return res
        stack=[root]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.children:
                for child in reversed(node.children):
                    stack.append(child)

        return res
#递归法
"""
    def order(self, res: List[int], node: 'Node') -> List[int]:
        if node is None:
            return res
        res.append(node.val)
        if node.children:
            for child in node.children:
                self.order(res, child)
        return res

    def preorder(self, root: 'Node') -> List[int]:
        res = []
        return self.order(res, root)
"""
sol=Solution()
root=Node(1)
root.children=[Node(3),Node(2),Node(4),Node(None)]
root.children[0].children=[Node(5),Node(6)]
print(sol.preorder(root))