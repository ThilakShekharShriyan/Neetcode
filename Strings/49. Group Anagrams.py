


#https://leetcode.com/problems/group-anagrams/description/


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dMap = defaultdict(list)
        ans = list()


        for i in strs:

            sortedString = sorted(i) #list of sorted char
            sortedString = ''.join(sortedString)
            dMap[sortedString].append(i)
        
        for i in dMap:
            ans.append(dMap[i])

        return ans


