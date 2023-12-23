class Solution:
    def isPathCrossing(self, path: str) -> bool:
        fun=[]
        a=0
        b=0
        fun.append((0,0))
        for i in path:
            if i=="N":
                b+=1
            elif i=="E":
                a+=1
            elif i=="W":
                a-=1
            else:
                b-=1
            if(a,b) in fun:
                return True
            else:
                fun.append((a,b))
        return False     