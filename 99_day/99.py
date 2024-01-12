class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        fun = [""]

        for char in s:
            if char.isdigit():
                for i in range(len(fun)):
                    fun[i] += char
            else:
                n = len(fun)
                for i in range(n):
                    fun.append(fun[i] + char.lower())
                    fun[i] += char.upper()

        return fun