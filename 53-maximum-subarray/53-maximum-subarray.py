class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
    
    # curr = -2, 0, 1, -2, 4, 3, 5, 6, 1, 5
    # max = -2, 1, 1, 4, 4, 5, 6, 6, 6