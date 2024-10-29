#https://leetcode.com/problems/palindrome-linked-list/description/


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


        slow , fast = head , head

        #slow is at middle and fast is at the last node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse the second half

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        left , right = head , prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
