class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal_cnt = 0 
        vertical_cnt = 0 

        n = len(moves) 

        if n % 2 != 0: 
            return False

        for move in moves: 
            if move == "U": 
                vertical_cnt += 1
            elif move == "D": 
                vertical_cnt -= 1
            elif move == "L":
                horizontal_cnt -= 1
            else: 
                horizontal_cnt += 1
        
        return vertical_cnt == 0 and horizontal_cnt == 0