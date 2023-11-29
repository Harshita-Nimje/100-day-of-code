class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        a=0
        for i in range (len(num[::-1])):
            if num[-1-i] =="0":
                a += 1
            else:
                break
        return num[:len(num)-a]