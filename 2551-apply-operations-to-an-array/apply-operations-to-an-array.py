class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        r=0
        for w in range (len(nums)-1):
            if nums[w]==nums[w+1]:
                nums[w]*=2
                nums[w+1]=0
            
        for w in range (len(nums)):
            if nums[w]!=0 : 
                nums[r],nums[w]=nums[w],nums[r]
                r+=1
        return nums
        