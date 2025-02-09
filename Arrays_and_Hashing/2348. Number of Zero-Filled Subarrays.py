class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        i , res = 0 , 0

        while i < len(nums):
            ctr = 0
            while i < len(nums) and nums[i]==0:
                ctr+=1
                i+=1
                res +=ctr
            i+=1

        return res