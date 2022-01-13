class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # TopDown T:O(n*m) S:O(n *m)
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         dp = [[0 for _ in range(n)] for _ in range(m)]
        
#         for c in range(n):
#             if obstacleGrid[0][c] == 1:
#                 break
#             dp[0][c] = 1
        
#         for r in range(m):
#             if obstacleGrid[r][0] == 1:
#                 break
#             dp[r][0] = 1
        
#         for r in range(1,m):
#             for c in range(1,n):
#                 if obstacleGrid[r][c] == 1:
#                     continue
#                 dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
#         return dp[-1][-1]
#         TopDown with Space Optimized T:O(n*m) S:O(1)
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        
        for c in range(1,n):
            obstacleGrid[0][c] = int(obstacleGrid[0][c] == 0 and obstacleGrid[0][c -1] == 1)
            
        for r in range(1,m):
            obstacleGrid[r][0] = int(obstacleGrid[r][0] == 0 and obstacleGrid[r - 1][0] == 1)
        
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 0:
                    obstacleGrid[r][c] = obstacleGrid[r][c -1] + obstacleGrid[r -1][c]
                else:
                    obstacleGrid[r][c] = 0
                    
        return obstacleGrid[-1][-1]