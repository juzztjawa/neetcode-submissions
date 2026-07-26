class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        maxarea=0
        area = 0
        while l<r:
            area = (r-l)*(min(heights[l],heights[r]))
            maxarea = max(area,maxarea)
            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
        return maxarea