class Solution:
    def coloredCells(self, n: int) -> int:
        fun = n*n
        dum = (n-1)*(n-1)
        return fun + dum