class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        doom=len(nums)
        return ((nums[doom-2]*nums[doom-1])-(nums[0]*nums[1]))