class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        fun = ''
        for i in words:
            fun += i[0]
        
        if fun == s:
            return True
        else:
            return False  