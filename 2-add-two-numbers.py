from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sumListnode(self,l: ListNode)->int:
        nums=[]
        while l:
            nums.append(l.val)
            l=l.next
        num=0
        for i in range(len(nums)):
            num+=nums[i]*(10**i)
        return num
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num=self.sumListnode(l1)+self.sumListnode(l2)
        res=[]
        while num>0:
            res.append(num%10)
            num=num//10
        dummy = ListNode(0)
        cur=dummy
        for node in res:
            cur.next=ListNode(node)
            cur=cur.next
        return dummy.next
l1=ListNode(9)
l1.next=ListNode(9)
l1.next.next=ListNode(9)
l2=ListNode(9)
solu=Solution()
print(solu.addTwoNumbers(l1,l2))