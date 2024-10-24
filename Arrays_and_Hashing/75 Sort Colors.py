# https://leetcode.com/problems/sort-colors/

nums = [1,2,0]

i , n = 0 , len(nums)

while i < n:

    if nums[i] == 0:
        del(nums[i])
        nums.insert(0 , 0)
        i+=1
    elif nums[i] == 2:
        del(nums[i])
        nums.append(2)
        n-=1
    elif nums[i] == 1:
        i+=1
    print( i , n , nums)
