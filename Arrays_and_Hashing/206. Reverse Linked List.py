

#https://leetcode.com/problems/reverse-linked-list/description/



prev , cur = None , head

while cur:

    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev