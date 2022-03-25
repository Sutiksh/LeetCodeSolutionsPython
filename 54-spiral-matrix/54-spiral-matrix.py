class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        m,n = len(matrix),len(matrix[0])
        top = matrix[0]
        left = [row[0] for row in matrix[1:m]][::-1] if n > 1 else []
        right = [row[-1] for row in matrix[1:m]]
        bottom = matrix[m-1][1:n-1][::-1] if m > 1 else []
        
        stripped = [row[1:n-1] for row in matrix[1:m-1] if len(row[1:n-1]) > 0]
        sequence = top+right+bottom+left+self.spiralOrder(stripped)
        return sequence
            
            

            
        