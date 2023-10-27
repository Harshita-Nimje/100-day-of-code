class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fun=set()
        for num in nums:
            if num in fun:
                return num      
            fun.add(num)  