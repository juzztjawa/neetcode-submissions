class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n -1
        leftmax = height[l]
        rightmax = height[r]
        res = 0
        while l < r:
            if leftmax > rightmax:
                r-=1
                rightmax = max(rightmax,height[r])
                res += rightmax - height[r]
            else:
                l+=1
                leftmax = max(leftmax,height[l])
                res+= leftmax - height[l]
        return res
            
