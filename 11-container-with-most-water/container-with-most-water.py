class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_w=0
        while l<r:
            w=r-l
            ch=min(height[l],height[r])
            c_w=w*ch
            max_w=max(max_w,c_w)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_w
