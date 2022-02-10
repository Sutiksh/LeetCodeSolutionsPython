class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lsf = float("inf")
        for p in prices:
            if p < lsf:
                lsf = p
                continue
            profit = max(profit, p - lsf)
        
        return profit