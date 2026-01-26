class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        T = collections.defaultdict(set)
        for u,v,w in allowed: 
            T[u,v].add(w)
        
        seen = set() 

        def solve(row): 
            if len(row) == 1: return True 
            if row in seen: return False 

            seen.add(row) 

            next_row = []

            def build(idx): 
                if idx + 1 == len(row): return solve("".join(next_row))

                for top in T[row[idx], row[idx + 1]]: 
                    next_row.append(top)
                    if build(idx + 1): 
                        return True 
                    next_row.pop()
                
                return False 

            return build(0)
        
        return solve(bottom)
