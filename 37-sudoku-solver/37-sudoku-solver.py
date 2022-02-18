class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty_pos = [] # record positions that are not filled with digit
        d = collections.defaultdict(int) # check valid sudoku
        digits = [str(i) for i in range(1, 10)] # all possible digits
        
        def backtrack(i):
            r, c = empty_pos[i]

            for digit in digits:
                # the case that cannot put `digit` into `pseudo-board[r][c]`
                if d[(r, digit)] or d[(digit, c)] or d[(r//3, c//3, digit)]:
                    continue

                # try to put `digit` in `pseudo-board[r][c]`
                d[(r, digit)] = d[(digit, c)] = d[(r//3, c//3, digit)] = 1

                # if all empty positions are filled / backtrack find the solution
                if not i or backtrack(i - 1):
                    board[r][c] = digit
                    return True

                # remove `digit` in `pseudo-board[r][c]`
                d[(r, digit)] = d[(digit, c)] = d[(r//3, c//3, digit)] = 0

            # the case that cannot put any `digit` into `pseudo-board[r][c]`
            return False
        
        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit != '.':
                    d[(r, digit)] = d[(digit, c)] = d[(r//3, c//3, digit)] = 1
                else:
                    empty_pos.append((r, c))

        backtrack(len(empty_pos) - 1)