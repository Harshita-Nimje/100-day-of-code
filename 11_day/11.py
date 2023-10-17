class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        z = ""
        for i in b:
            z+=f"{i}"
        return pow(a, int(z),1337)
              
