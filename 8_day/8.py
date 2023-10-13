class Solution:
    def pivotInteger(self, n: int) -> int:
        y=(n*n+n)//2
        x = int(math.sqrt(y))
        if (x * x == y):
            return x
        else: 
            return-1 