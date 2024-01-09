class Solution:
    def generateTheString(self, n: int) -> str:
        fun = ""
        if n % 2 == 0:
            for i in range(n-1):
                fun += "x"
            fun += "y"
        else:
            for i in range(n):
                fun += "x"
        return fun