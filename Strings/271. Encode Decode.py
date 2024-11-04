#https://leetcode.com/problems/encode-and-decode-strings/description/

class Solution:

    def encode(self, strs) -> str:

        ans = ""
        for i in strs:
            ans = ans + "\_" + i
        return ans


    def decode(self, s: str):

        return s.split("\_")[1:]