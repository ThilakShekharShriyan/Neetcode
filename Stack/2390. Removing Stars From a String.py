class Solution:
    def removeStars(self, s: str) -> str:

        curStack = []

        for i in s:
            if i == "*":
                curStack and curStack.pop()
            else:
                curStack.append(i)
        return "".join(curStack)

                
        