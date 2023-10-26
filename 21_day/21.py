class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fun=[]
        for i in nums:
            if i not in fun:
                fun.append(i)
            else:
                fun.remove(i)
        return fun[0]            