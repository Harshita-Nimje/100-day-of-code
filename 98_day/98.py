class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dum=[]
        for i in arr:
            if (arr.count(i)==1):
                dum.append(i)
        if k>len(dum):
            return ""
        else:
            return dum[k-1]                   