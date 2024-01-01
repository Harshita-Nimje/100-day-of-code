class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        fun =a=b=0
        g.sort()
        s.sort()
        while a<len(g) and b<len(s):
            if g[a] <= s[b]:
                fun+=1
                a+=1
            b+=1
        return fun        
