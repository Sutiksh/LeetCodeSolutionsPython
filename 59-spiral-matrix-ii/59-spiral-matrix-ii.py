class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        m = n-1 # max index
        cur = 1
        
        # For each layer
        for i in range(n // 2 + 1):
            offset = m - i*2 # offset for each side
            
            for j in range(i, m-i): # For each cell on one side
                # Update corresponding position at all 4 sides
                matrix[i][j] = cur
                matrix[j][m-i] = cur + offset
                matrix[m-i][m-j] = cur + offset * 2
                matrix[m-j][i] = cur + offset * 3
                cur += 1
            cur += offset * 3 # Wrap up current layer
                
        # Fill center if n is odd
        if n % 2 == 1:
            matrix[n//2][n//2] = cur
        
        return matrix