class Solution:
    def firstUniqChar(self, s: str) -> int:
        for fun in range(len(s)):
            if s.count(s[fun])==1:
                return fun
        return -1          
