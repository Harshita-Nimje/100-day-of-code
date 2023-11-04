class Solution:
    def removeStars(self, s: str) -> str:
        fun=[]
        for i in s:
            if i!='*':
                fun.append(i)
            else:
                fun.pop()
        return ''.join(fun)            
