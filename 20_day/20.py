class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        fun=1
        while fun<n:
            fun*=4
        return fun==n