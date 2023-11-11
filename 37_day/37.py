class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = len(nums)
        fun=[]
        s=set(nums)
        for i in range(1, x+1):
            fun.append(i)

        s=set(nums)
        not_fun =[]
        for j in fun:
            if j not in s:
                not_fun.append(j)
        return not_fun     