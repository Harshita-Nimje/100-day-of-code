class Solution:
    def isThree(self, n: int) -> bool:
        fun=0
        for i in range(1,n+1):
            if n%i==0:
                fun+=1
            if fun>3:
                return False
        return fun==3 