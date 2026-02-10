# Approach: Iterate by sorted indices
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(s)

        def occurs(idx, src): 
            src_len = len(src)
            
            if idx + src_len > n: return False
            
            src_idx = 0
            for i in range(idx, idx + src_len): 
                if s[i] != src[src_idx]: return False 
                src_idx += 1
            
            return True

        triplets = sorted(zip(indices, sources, targets))

        res = []
        prev = 0  

        for idx, src, tgt in triplets:
            res.append(s[prev:idx])

            if occurs(idx, src):
                res.append(tgt)
                prev = idx + len(src)
            else:
                if idx > prev: 
                    prev = idx
                    
        res.append(s[prev:])
        return "".join(res)
