class Solution:
    def largestOddNumber(self, num: str) -> str:
        fun=-1
        for i in range (len(num)):
            if int(num[i])%2!=0:
                fun=i
        if fun==-1:
            return ""    
        else:    
            return str(num[0:fun+1])              
                  