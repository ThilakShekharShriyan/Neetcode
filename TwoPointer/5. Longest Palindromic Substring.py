#https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=two-pointers


class Solution:
    def longestPalindrome(self, s: str) -> str:


        res = ""
        resLen = 0

        for i in range(len(s)):

            #check for odd 
            l , r = i , i
            while l >=0 and r < len(s) and s[l]==s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l-=1
                r+=1

            #Even 
            l , r = i , i+1
            while l >=0 and r < len(s) and s[l]==s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l-=1
                r+=1

        return res
            




        