class Solution:
    def partitionString(self, s: str) -> int:
        res = []

        check = set()
        ss = ""
        for i in s:
            if i in check:
                res.append(ss)
                ss=""
                check.clear()
            ss += i
            check.add(i)
        if s != "":
            res.append(s)

        return len(res)

----- 

class Solution:
    def partitionString(self, s: str) -> int:

        res = 1
        curSet = set()

        for i in s:
            if i in curSet:
                res+=1
                curSet.clear()
            curSet.add(i)
        return res