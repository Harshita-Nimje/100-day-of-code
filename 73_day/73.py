class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        fun = sorted(list(str(n)))
        for i in range(30):
            fun1 = 2**i
            fun2 = sorted(list(str(fun1)))
            if fun ==fun2:
                return True