#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operations = ["+" , "-" , "*" , "/"]

        for i in tokens:

            if i not in operations:
                stack.append(i)
            else:
                l , r = int(stack.pop()) , int(stack.pop())
                match i:
                    case "+":
                        val = r + l
                    case "*":
                        val = r * l
                    case "/":
                        val =r / l 
                    case "-":
                        val = r - l
                stack.append(val)
        
        return int(stack[0])
                       