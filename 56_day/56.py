class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n=sentence.split(" ")
        for i in range(len(n)):
            if searchWord == n[i][0:len(searchWord)]:
                return i+1
        return -1        