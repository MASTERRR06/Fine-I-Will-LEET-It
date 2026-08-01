class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=0
        for w in range(len(nums)):
            if nums[w]!= val:
                nums[r],nums[w]=nums[w], nums[r]
                r+=1
        return r


        