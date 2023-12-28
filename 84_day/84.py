class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        fun=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    num=(nums[i]-nums[j])*nums[k]
                    fun=max(fun,num)
        return fun  