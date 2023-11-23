class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low=[]
        high=[]
        equal=[]
        for i in nums:
            if i > pivot:
                high.append(i)
            if i < pivot:
                low.append(i) 
            if i==pivot:
                equal.append(i)    
        ans=low+equal+high
        return ans   
