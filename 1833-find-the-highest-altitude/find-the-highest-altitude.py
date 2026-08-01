class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=0
        r=0
        for move in gain:
            l+=move
            if l>r:
                r=l
        return r