class Solution:
    def removeDuplicates(self, s: str) -> str:
        fun=[]
        for i in s:
            if len(fun)>0 and fun[-1]==i:
                fun.pop()
            else:
                fun.append(i)    
        return ("".join(fun))  