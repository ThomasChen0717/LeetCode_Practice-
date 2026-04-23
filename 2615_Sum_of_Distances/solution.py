# Approach 1: Brute Force
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_to_index = collections.defaultdict(list)

        for i, num in enumerate(nums): 
            num_to_index[num].append(i) 
        
        res = []
        for i, num in enumerate(nums): 
            distance = 0
            for idx in num_to_index[num]: 
                if idx != i: 
                    distance += abs(idx - i) 
            
            res.append(distance)
        
        return res

# Approach 2: Prefix Sum 
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num_to_index = collections.defaultdict(list)

        for i, num in enumerate(nums): 
            num_to_index[num].append(i) 
        
        res = [0] * len(nums)
        for indices in num_to_index.values(): 
            n = len(indices)
            prefix_sum = [0] * (n + 1)

            for i in range(n):
                prefix_sum[i+1] = prefix_sum[i] + indices[i]
            
            for i in range(n): 
                idx = indices[i]
                left_dist = i * idx - prefix_sum[i] 
                right_dist = (prefix_sum[n] - prefix_sum[i+1]) - idx * (n - i - 1)

                res[idx] = left_dist + right_dist

        return res
            