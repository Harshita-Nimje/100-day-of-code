class Solution:
    def maxScore(self, s: str) -> int:
        fun=0
        not_fun=0
        notnot_fun=s.count("1")
        for i in range(len(s)-1):
            if s[i]=="0":
                not_fun+=1
            else:
                notnot_fun-=1
            fun=max(fun,not_fun+notnot_fun)
        return fun 