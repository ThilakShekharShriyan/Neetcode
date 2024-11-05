#https://leetcode.com/problems/sqrtx/description/


l , r = 0 , x
ans = 0

while l <= r:

    m = l + ((r-l)//2)
    if m **2 > x:
        r = m -1
    elif m **2 < x:
        l = m+1
        ans = m
    else:
        print (m)
        break
print( ans)