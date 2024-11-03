

#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/




nums = [-1,0,1,2,-1,-4]
ans = list()
nums.sort()

#[-1,0,1,2,-1,-4]
#[-4,-1,-1,0,1,2]
i = 0
while i < len(nums)-1:
    print(i)

    l , r = i+1 , len(nums)-1
    while l < r:
        if nums[i] + nums[l] + nums[r] == 0:
            ans.append([nums[i], nums[l], nums[r]])
            break
        elif nums[i] + nums[l] + nums[r] > 0:
            r-=1
        else:
            l+=1
        print(l , r)
    
    i+=1 
    while i < len(nums)-1 and nums[i] == nums[i+1]:
        i+=1

print(ans)