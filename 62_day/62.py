class Solution:
    def totalMoney(self, n: int) -> int:
        total=0
        monday=0
        for i in range (n):
            if i%7==0:
                monday=monday+1#i//7 +1
                total = total+monday
            else:
                total += i%7 + monday 
        return total         
                  