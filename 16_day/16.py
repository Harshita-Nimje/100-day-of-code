class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
            
        else:
            target=word.index(ch)
            target2=word[:target+1]
            iu=word[target+1:]
            yu=target2[::-1]
            return yu+iu