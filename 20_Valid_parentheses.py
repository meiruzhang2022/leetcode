class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=='(':
                stack.append(')')
            if char==')':
                if stack and stack[-1]==')':
                    stack.pop()
                else:
                    return False
            if char=='[':
                stack.append(']')
            if char==']':
                if stack and stack[-1]==']':
                    stack.pop()
                else:
                    return False
            if char=='{':
                stack.append('}')
            if char=='}':
                if stack and stack[-1]=='}':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
sol=Solution()
print(sol.isValid("([])"))
