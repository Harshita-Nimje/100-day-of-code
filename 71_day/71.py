class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        fun=[]
        for i in nums:
            if i in fun:
                return i
            else:
                fun.append(i)   