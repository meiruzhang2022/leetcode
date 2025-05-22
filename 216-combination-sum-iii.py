from typing import List
class Solution:
    def back(self,k,n,start,temp,res,sum) -> List[List[int]]:
        if len(temp)==k and sum==n:
            res.append(temp[:])
            sum=0
            return
        for i in range(start,10):
            if i>=n:
                break
            else:
                sum+=i
                if sum>n:
                    break
                else:
                    temp.append(i)
                    self.back(k,n,i+1,temp,res,sum)
                    sum-=temp[-1]
                    temp.pop()
        return res
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.back(k,n,1,[],[],0)
n=7
k=3
s=Solution()
print(s.combinationSum3(k,n))