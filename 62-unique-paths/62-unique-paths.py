class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #TopDown T:O(n*m) S:O(n*m)
#         dp = [[0 for _ in range(n)]for _ in range(m)]
        
#         for c in range(n):
#             dp[0][c] = 1
        
#         for r in range(m):
#             dp[r][0] = 1
            
#         for r in range(1,m):
#             for c in range(1,n):
#                 dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
#         return dp[-1][-1]
        
        # BottomUp T:O(n*m) S:(n)
        row = [1] * n
        for r in range(1,m):
            newRow = [1]*n
            for c in range(n - 2,-1,-1):
                newRow[c] = newRow[c + 1] + row[c]
            row = newRow
        
        return row[0]