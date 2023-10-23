class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fun=nums1+nums2
        fun.sort()
        start=0
        end=len(fun)-1
        while start<end:
            start+=1
            end-=1
        if start==end:
            return float(fun[start])
        else:
            return float ((fun[start]+fun[end])/2) 