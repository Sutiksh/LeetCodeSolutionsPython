class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(9):
            num = [x for x in board[row] if x != "."]
            if len(num) != len(set(num)):
                return False
        
        # Check columns
        for col in range(9):
            num = [x[col] for x in board if x[col] != "."]
            if len(num) != len(set(num)):
                return False
        
        # Check sub-matrices
        r = [[0,1,2],[3,4,5],[6,7,8]]
        
        for i in range(3):
            for j in range(3):
                num = [board[a][b] for a in r[i] for b in r[j] if board[a][b] != "."]
                if len(num) != len(set(num)):
                    return False
                
        return True