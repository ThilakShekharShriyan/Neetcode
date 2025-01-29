#https://leetcode.com/problems/maximum-sum-circular-subarray/description/


#Brute Force

                # nums = [5,-3,5]

                # n = len(nums)
                # visited = set()
                # ansSet = []

                # for i in range(len(nums)):

                #     j = i
                #     visited.clear()
                #     maxSum = nums[i]
                #     curSum = 0
                #     while j % n not in visited:

                #         if curSum < 0:
                #             curSum = 0
                #         curSum += nums[j%n]
                #         maxSum = max(maxSum , curSum)
                #         visited.add(j%n)
                #         print( j , visited)
                #         j+=1
                #     ansSet.append(maxSum)

                # print(max(ansSet))
                
#Using Min Max Approach Neetcode


nums = [5,-3,5]


curMax , curMin , n  = 0 , 0 , len(nums)
globalMin , globalMax = nums[0] , nums[0]

for i in range(n):
    