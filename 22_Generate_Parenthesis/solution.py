# Approach 1: Backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [] 

        def backtrack(curr, left_br_cnt, right_br_cnt): 
            if len(curr) == 2 * n: ans.append(curr)  

            if left_br_cnt < n: 
                backtrack(curr + '(', left_br_cnt + 1, right_br_cnt) 
            
            if right_br_cnt < left_br_cnt:
                backtrack(curr + ')', left_br_cnt, right_br_cnt + 1) 


        backtrack("", 0, 0)
        return ans 

# Apporach 2: Divide and Conquer
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        answer = []
        for left_count in range(n):
            for left_string in self.generateParenthesis(left_count):
                for right_string in self.generateParenthesis(
                    n - 1 - left_count
                ):
                    answer.append(left_string + "("  + right_string + ")")

        return answer