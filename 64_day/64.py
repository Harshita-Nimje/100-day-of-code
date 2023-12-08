class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        fun=nums[0]
        for i in nums[1:]:
            fun^=i
        return fun   
        