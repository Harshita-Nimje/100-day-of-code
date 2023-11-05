class Solution:
    def repeatedCharacter(self, s: str) -> str:
        fun=[]
        for i in s:
            if i in fun:
                return i
            else:
                fun.append(i)          
