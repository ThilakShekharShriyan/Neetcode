# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        q = deque([root])

        while q:
            cur = q.popleft()

            if cur:

                q.append(cur.left)
                q.append(cur.right)

            else:
                while q:
                    if q.popleft():
                        return False

        return True
            


        