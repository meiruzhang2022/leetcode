from typing import List
class Solution:
    def backtrack(self,trans,res,temp_str:str,i)->List[str]:
        if len(temp_str)==len(trans):
            res.append(temp_str)
            return []

        while i < len(trans):
            for j in range(len(trans[i])):
                temp_str+=(trans[i][j])
                self.backtrack(trans,res,temp_str,i+1)
                temp_str=temp_str[:-1]
            i+=1
        return res
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        trans=[]
        for char in digits:
            if char in dic:
                trans.append(dic[char])
        return self.backtrack(trans,[],"",0)
dights=""
s=Solution()
print(s.letterCombinations(dights))