class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ts=sum(nums)
        l=0
        for x in range (len(nums)):
            r=ts-l-nums[x]
            if (l==r):
                return x
            l+=nums[x]
        
        return -1
        