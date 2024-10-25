
from math import ceil

nums = [-1,0,3,5,9,12]
target = 9
l , r = 0 , len(nums)

while l <= r:

    mid = ((r-l)//2)+1
    if nums[mid] == target:
        print(mid)
    elif nums[mid] > target:
        r = mid
    else:
        l = mid

print(-1)