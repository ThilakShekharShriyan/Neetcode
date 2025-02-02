class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:


        res = []
        for i in spells:
            ctr = 0
            for j in potions:
                if i * j >= success:
                    ctr+=1
            res.append(ctr)
        
        return res
            
        
----


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        res = []
        potions.sort()


        for i in spells:

            l ,r = 0 , len(potions)-1
            idx = len(potions)

            while l <= r:
                m = l + (r-l)//2

                if i * potions[m] >= success:
                    r = m-1
                    idx = m
                else:
                    l = m+1
            res.append(len(potions)-idx)
        return res

        