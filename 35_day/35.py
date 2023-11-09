class Solution:
    def alternateDigitSum(self, n: int) -> int:
        fun1=str(n)
        fun=0
        for i in range(len(fun1)):
            if i%2==0:
                fun=fun+int(fun1[i])
            else:
                fun=fun-int(fun1[i])
        return fun 