class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low,high=0, len(numbers)-1
        while low<=high  :
            sums=numbers[low]+numbers[high]
            if(sums==target):
                fun=[low+1,high+1]
                return fun
            if sums < target:
                low+=1
            else:
                high-=1 
        return fun                  