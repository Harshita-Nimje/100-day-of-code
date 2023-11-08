class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        fun = 0
        
        for i in range(0, len(arr)):
            if arr[i] %2 != 0:
                fun += 1
                if fun == 3:
                    return True
            else:
                fun = 0
        return False 