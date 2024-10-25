

#https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:


    def mergeTwoLists(self, list1, list2):


        AnsKey = ListNode()
        temp = AnsKey


        while list1 != None and list2 != None:

            temp.next = ListNode()
            temp = temp.next

            if list1.val <= list2.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            
            
        
        if list1 != None:
            temp.next = list1
        elif list2 != None:
            temp.next = list2

        return AnsKey.next


