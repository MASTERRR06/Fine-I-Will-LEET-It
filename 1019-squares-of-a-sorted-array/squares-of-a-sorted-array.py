class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        res=[0]*len(nums)
        p=len(nums)-1
        while l<=r:
            ls=nums[l]**2
            rs=nums[r]**2
            if ls>rs:
                res[p]=ls
                l+=1
            else:
                res[p]=rs
                r-=1
            p-=1
        return res
        