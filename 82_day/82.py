class Solution:
    def reverseWords(self, s: str) -> str:
        fun=s.split()
        fun.reverse()
        return ' '.join(fun)