class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        fun=0
        for i in range(len(s)):
            if i<len(s)//2:
                if s[i] in "aeiouAEIOU":
                    fun-=1
            else:
                if s[i] in "aeiouAEIOU":
                    fun+=1
        return fun==0
        