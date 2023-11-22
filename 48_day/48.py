class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)<=1:return pref   
        not_fun=pref[0]
        for i in range(1,len(pref)):
            fun=pref[i]
            pref[i] = not_fun^pref[i]
            not_fun = fun
        return pref
