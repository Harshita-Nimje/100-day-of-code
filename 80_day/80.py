class Solution:
    def minOperations(self, s: str) -> int:
        fun=0
        not_fun=0

        for i in range(len(s)):
            if i%2==0:
                if s[i] == "1":
                    fun +=1
                else:
                    not_fun+=1
            else:
                if s[i] == "1":
                    not_fun +=1
                else:
                    fun +=1
        a=min(fun,not_fun)
        return a                        
 