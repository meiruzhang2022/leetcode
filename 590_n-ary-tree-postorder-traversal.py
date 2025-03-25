from typing import Optional,List
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def order(self,res:List[int],node:'Node')-> List[int]:
        if node is None:
            return res
        if node.children:
            for child in node.children:
                self.order(res,child)
        res.append(node.val)
        return res
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        return self.order(res,root)
sol=Solution()
root=Node(1)
root.children=[Node(3),Node(2),Node(4),Node(None)]
root.children[0].children=[Node(5),Node(6)]
print(sol.postorder(root))