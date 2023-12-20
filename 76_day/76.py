class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_left=0
        count_right=0
        for i in s:
            if i == 'R':
                count_right +=1
            else:
                count_right -=1
            if count_right ==0:
                count_left +=1
        return count_left    