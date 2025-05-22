from typing import List
class Solution:
    def backtracking(self,start:int,res:List[List[int]],temp:List[int],k,end):
        if len(temp) ==k:
            res.append(temp[:])
            return True
        for i in range(start,end):
            temp.append(i)
            self.backtracking(i+1,res,temp,k,end)
            temp.pop()
        return res
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.backtracking(1,[],[],k,n+1)

n=4
k=2
print(Solution().combine(n,k))