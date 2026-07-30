class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        c_sum=0
        for nums in nums:
            if nums==1:
                c_sum+=1
                if c_sum>max:
                    max=c_sum
            else:
                c_sum=0
        return max
        