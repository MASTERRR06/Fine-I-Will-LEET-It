class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=len(digits)-1
        for nums in reversed(digits):
            if digits[x]<9:
                digits[x]+=1
                return digits
            else:
                digits[x]=0
            x-=1
        return [1]+digits
        