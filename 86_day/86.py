class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        fun=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i!=j:
                    fun+=1
        return fun