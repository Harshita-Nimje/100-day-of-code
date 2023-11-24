class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins<costs[0]:
            return 0
        iceC=0
        total=0
        for i in costs:
            total+=i
            if total <= coins:
                iceC+=1
        return iceC             
