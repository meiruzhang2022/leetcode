from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index=0
        for num in s:
            if index<len(g) and num>=g[index]:
                index+=1
        return index
g=[1,2,3]
s=[1,1,1]
sol=Solution()
print(sol.findContentChildren(g,s))