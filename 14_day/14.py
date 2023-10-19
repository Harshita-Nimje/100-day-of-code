class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fun=0
        for i in nums:
            if i!=val:
                nums[fun]=i
                fun+=1
        return fun        
            