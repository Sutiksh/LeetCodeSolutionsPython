class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        @lru_cache(None)
        
        def helper(i,j):
            if i==0 and j==0:
                return grid[i][j]
            if i<0 or j<0:
                return float("inf")
            
            return grid[i][j]+min(helper(i-1,j),helper(i,j-1))
        
        return helper(m-1,n-1)
            
            
            
        