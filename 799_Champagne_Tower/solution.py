# Approach: Simulation
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * k for k in range(1, query_row + 2)]

        tower[0][0] = poured 

        for i in range(len(tower) - 1): 
            for j in range(len(tower[i])): 
                full = (tower[i][j] - 1.0) / 2.0

                if full > 0: 
                    tower[i+1][j] += full
                    tower[i+1][j+1] += full 
        
        return min(1, tower[query_row][query_glass])