# Approach 1: Follow the rules
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit, seen_exponent, seen_dot = False, False, False

        for i, ch in enumerate(s):
            if ch.isdigit(): 
                seen_digit = True
            elif ch in ['+', '-']: 
                if i != 0 and s[i-1] != 'e' and s[i-1] != 'E': 
                    return False 
            elif ch == '.': 
                if seen_dot or seen_exponent: return False 
                else: seen_dot = True 
            elif ch == 'e' or ch == 'E': 
                if seen_exponent or not seen_digit: return False 
                else: 
                    seen_exponent = True
                    seen_digit = False 
            else:
                return False
        
        return seen_digit
            
# Approach 2: Deterministic Finite Automaton(DFA)
class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 7, "digit": 6},
            {"digit": 6},
            {"digit": 6},
        ] 

        curr_state = 0

        for ch in s: 
            if ch.isdigit():
                group = "digit" 
            elif ch in ['+','-']:
                group = "sign"
            elif ch == '.': 
                group = "dot"
            elif ch in ['e','E']: 
                group = "exponent"
            else:
                return False 
        
            if group not in dfa[curr_state]:
                return False
            
            curr_state = dfa[curr_state][group]
        
        return curr_state in [1, 4, 6]
            