class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = []
        d = []
        
        for i in paths:
            s.append(i[0])
            d.append(i[1])
        for i in d:
            if i not in s:
                return i