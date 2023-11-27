class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        fun=0
        not_fun=len(nums)

        for i in range(not_fun-1):
            if (i-fun)%2==0 and nums[i]==nums[i+1]:
                fun+=1
        return fun+1 if (not_fun-fun)%2==1 else fun        