class Solution:
    def isPalindrome(self, x: int) -> bool:
        w = ""
        for i in str(x):
            w = i + w
        if w ==str(x):
            return True
        else:
            return False
