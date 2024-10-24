

#https://leetcode.com/problems/maximum-subarray/description/




def maxSubArray(self, nums) -> int:

    maxSum = nums[0]
    curSum = 0

    for i in nums:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSum = max(curSum , maxSum)
    return maxSum


            
        