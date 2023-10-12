import numpy as np
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        new_ans=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    new_ans.append(j)
                elif i!=j & j not in arr2 and arr2.index(i)==0:
                    ans.append(j)    
                    
        return new_ans+sorted(ans)   