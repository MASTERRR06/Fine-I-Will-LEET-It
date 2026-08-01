class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums)<2):
            return len(nums)
        r=2
        for w in range(2, len(nums)):
            # Look behind check: Compare against the element 2 slots back from our writer!
            if nums[w] != nums[r - 2]:
                nums[r] = nums[w]  # Write the valid number forward
                r += 1             # Move our writer slot forward
                
        return r  # Return the count of elements kept
        