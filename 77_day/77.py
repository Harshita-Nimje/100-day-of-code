class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if sorted(prices)[0] + sorted(prices)[1] <= money :
            return money - (sorted(prices)[0] + sorted(prices)[1])
        else :
            return money