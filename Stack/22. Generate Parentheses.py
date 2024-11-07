#https://leetcode.com/problems/generate-parentheses/description/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        




        stack =[]
        res = []


        def backTrack(openCtr , closedCtr):


            if openCtr == closedCtr == n:
                res.append("".join(stack))
                return
        
            if openCtr < n:
                stack.append("(")
                backTrack(openCtr+1 , closedCtr)
                stack.pop()
            
            if closedCtr < openCtr:
                stack.append(")")
                backTrack(openCtr , closedCtr + 1)
                stack.pop()
        backTrack(0,0)

        return res
