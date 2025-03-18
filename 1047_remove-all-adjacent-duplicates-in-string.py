#stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for char in s:
            if stack and char==stack[-1]:
                stack.pop()
                continue
            else:
                stack.append(char)
        return ''.join(stack)

#双指针
class Solution:
    def removeDuplicates(self, s: str) -> str:
        temp=list(s)
        fast=slow=0
        length=len(temp)
        while fast <length:
            temp[slow]=temp[fast]
            if slow>0 and temp[slow]==temp[slow-1]:
                slow-=1
            else:
                slow+=1
            fast+=1
        return ''.join(temp[:slow])
