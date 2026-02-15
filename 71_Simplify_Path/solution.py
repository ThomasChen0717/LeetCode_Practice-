# Approach: Stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for comp in path.split("/"): 
            if comp == "..": 
                if stack: 
                    stack.pop()
            elif comp == "." or not comp: 
                continue
            else: 
                stack.append(comp)
        
        final_str = "/" + "/".join(stack)
        return final_str