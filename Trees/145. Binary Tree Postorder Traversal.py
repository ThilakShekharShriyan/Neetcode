#https://leetcode.com/problems/binary-tree-postorder-traversal/description/



        stack = [root]
        visit = [False]
        res = []


        while stack:
            cur , v = stack.pop() , visit.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)
        return res