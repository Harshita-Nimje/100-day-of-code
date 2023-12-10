class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        fun=' '
        for i in digits:
            fun=fun+str(i)
        fun1=int(fun)+1
        fun=str(fun1)
        not_fun=[]
        for i in fun:
            not_fun.append(int(i))
        return not_fun        