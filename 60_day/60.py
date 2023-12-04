class Solution:
    def largestGoodInteger(self, num: str) -> str:
        fun=[]
        for i in range (len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                fun.append(num[i])
        if len(fun)==0:
            return ""
        else:
            return max((fun))*3