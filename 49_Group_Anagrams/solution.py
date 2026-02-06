# Approach 1: Categorize by Sorted String
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: Dict[str, List[str]] = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())

# Approach 2: Categorize by Count
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())
