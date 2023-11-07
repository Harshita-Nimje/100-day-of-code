class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def juh(s):
            fun=[]
            for i in s:
                if i=='#' and fun:
                    fun.pop()
                elif i !='#':
                    fun.append(i)
            return fun        
        return juh(s) == juh(t) 