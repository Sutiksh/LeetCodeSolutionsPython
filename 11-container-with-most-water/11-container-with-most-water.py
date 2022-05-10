class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = []
        lo, hi = 0, len(height) - 1
        
        while lo < hi:
            if height[lo] < height[hi]:
                ans = (hi - lo) * height[lo]
                res.append(ans)
                lo += 1
            elif height[lo] == height[hi]:
                ans = (hi - lo) * height[lo]
                res.append(ans)
                lo += 1
                hi -= 1
            else:
                ans = (hi - lo) * height[hi]
                res.append(ans)
                hi -= 1
            
        return max(res)
        