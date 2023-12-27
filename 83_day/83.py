class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        fun=len(arr)
        not_fun=0
        while not_fun < fun:
            if arr[not_fun] ==0:
                arr.insert(not_fun+1,0)
                arr.pop()
                not_fun+=1
            not_fun +=1    