# Approach: Backtracking
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(sm, lst, idx):
            if sm == target:
                res.append(lst.copy())
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                if sm + candidates[i] > target:
                    break

                lst.append(candidates[i])
                backtrack(sm + candidates[i], lst, i + 1)
                lst.pop()

        backtrack(0, [], 0)
        return res

