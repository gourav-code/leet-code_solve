class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        l = 0
        r = len(height)-1

        while l <r:
            result = max(result, min(height[r],height[l])*(r-l))
            if(height[l] < height[r]):
                l += 1
            elif(height[l]>=height[r]):
                r -= 1

        return result
        