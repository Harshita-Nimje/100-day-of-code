class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fun={}
        for i in strs:
            temp = ''.join(sorted(i))

            if temp not in fun:
                fun[temp] = [i]
            else:
                fun[temp].append(i)
        return fun.values()            