class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        fun = set()

        for i in nums:
            if i not in fun:
                fun.add(i)
            else:
                fun.remove(i)
        
        return list(fun)