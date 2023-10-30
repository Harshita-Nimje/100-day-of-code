class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        fun=0
        for i in s:
            if i==letter:
                fun+=1
        n=len(s)
        return int(fun/n*100)        