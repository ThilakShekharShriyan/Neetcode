class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        l , r = 0 , 0 

        # [7 , 8 , 9 , 10]
        # [5,6,7 , 8]

        while r < len(s) and l < len(g):

            if g[l] <= s[r]:
                l+=1
            r+=1
        return l

        
