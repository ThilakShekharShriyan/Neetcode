class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


        nums.append(float("-inf"))
        nums.insert(0 , float("-inf"))        
        l, m , r  = 0 ,1 , 2
        ans = 0
        print(nums)
        while r < len(nums):
            if nums[l] < nums[m] and nums[m] > nums[r]:
                ans = m-1
                return ans
            l+=1
            m+=1
            r+=1
        return ans