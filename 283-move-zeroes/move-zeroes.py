class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r=0 # to start reading from index 1
        #now what we have to do is compare each number and swap
        for w in range (len(nums)):# so that it runs the length of the whole array
            if nums[w]!=0:
                nums[r],nums[w]=nums[w],nums[r]
                r+=1

        return w
        