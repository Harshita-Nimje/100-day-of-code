class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            s = i.split()
            ans = max(len(s), ans)
        return ans   