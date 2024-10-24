# https://leetcode.com/problems/two-sum/description/


from collections import defaultdict
class Solution:
    def twoSum(self, nums, target):
        

        valuesTarget = defaultdict()

        for i , n  in enumerate(nums):
            if n in valuesTarget:
                return [i , valuesTarget[n]]
            else:
                valuesTarget[target - n] = i
        
