class Solution:
    def minimumSum(self, num: int) -> int:
        fun=sorted(str(num))
        fun="".join(fun)
        fun_1=fun[0]+fun[2]
        fun_2=fun[1] +fun[3]
        return int(fun_1) + int(fun_2)