


#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/



arr.append(-1)
mV = -1
for i in range(len(arr)-1 , -1 ,-1):

    if arr[i] > mV:
        mV = arr[i]
    else:
        arr[i] = mV

return arr[1:]


