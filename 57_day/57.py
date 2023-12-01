class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        fun=""
        for i in words:
            fun+=i
            if fun==s:
                return True
        return False        