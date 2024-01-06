# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        fun, dum = 1, n-1

        while fun <= dum:
            fun_dum = (dum + fun) // 2
            if isBadVersion(fun_dum)==False:
                fun = fun_dum+1
            else:
                dum = fun_dum - 1

        return fun