#https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:




        dp1 , dp2 = 1, 1

        for i in range(n-1):
            temp = dp1 + dp2
            dp1 = dp2
            dp2 = temp        
        return dp2
        