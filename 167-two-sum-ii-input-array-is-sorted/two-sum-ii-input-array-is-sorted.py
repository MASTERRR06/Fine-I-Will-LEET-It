class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            c_sum=nums[l]+nums[r]
            if c_sum==target:
                return[l+1,r+1]
            elif c_sum<target:
                l+=1
            else:
                r-=1
        return[]