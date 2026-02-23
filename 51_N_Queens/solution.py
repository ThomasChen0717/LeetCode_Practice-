# Approach: Backtracking
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def create_board(state):
            board = []
            for row in state: 
                board.append("".join(row)) 
            return board

        
        def backtrack(row, cols, diagonals, anti_diagonals, state): 
            if row == n: 
                res.append(create_board(state))
                return 
            
            for col in range(n): 
                curr_diag = row - col 
                curr_anti_diag = row + col 

                if col in cols or curr_diag in diagonals or curr_anti_diag in anti_diagonals: 
                    continue 
                
                cols.add(col)
                diagonals.add(curr_diag)
                anti_diagonals.add(curr_anti_diag) 

                state[row][col] = "Q" 

                backtrack(row + 1, cols, diagonals, anti_diagonals, state) 

                cols.remove(col)
                diagonals.remove(curr_diag)
                anti_diagonals.remove(curr_anti_diag) 
                state[row][col] = '.'
        
        res = [] 
        empty_board = [["."] * n for _ in range(n)] 
        backtrack(0, set(), set(), set(), empty_board)

        return res