class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        fun=1
        nums=set(nums)
        while fun in nums:
            fun +=1
        return fun    