class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        fun=[]
        while len(nums) > 0:
            dum=set(nums)
            fun.append(list(dum))
            for i in dum:
                nums.remove(i)
        return fun        