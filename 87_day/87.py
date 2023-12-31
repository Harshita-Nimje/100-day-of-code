class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        fun = -1
        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    fun = max(fun, right - left - 1)
        
        return fun