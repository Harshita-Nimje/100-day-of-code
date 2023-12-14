class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        fun=0
        for i in batteryPercentages:
            if i > fun:
                fun +=1
        return fun 