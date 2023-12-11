class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        fun={}
        for i in arr:
            if i in fun:
                fun[i]+=1
            else:
                fun[i]=1
        for i in fun:
            if fun[i]>(0.25*len(arr)):
                return i