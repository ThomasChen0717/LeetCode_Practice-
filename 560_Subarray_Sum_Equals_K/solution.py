# Approach 1: Brute Force 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0

        for start in range(len(nums)): 
            for end in range(start, len(nums)): 
                sm = 0
                for i in range(start, end + 1): 
                    sm += nums[i] 
                if sm == k: 
                    cnt += 1
        
        return cnt

# Approach 2: Cumulative Sum 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sm = [0] * (len(nums) + 1)
        sm[0] = 0

        for i in range(1, len(nums) + 1): 
            sm[i] = sm[i-1] + nums[i-1]

        for start in range(len(nums)): 
            for end in range(start, len(nums)): 
                if sm[end + 1] - sm[start] == k: 
                    cnt += 1
        return cnt

# Approach 3: Constant Space Cumulative Sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0

        for start in range(len(nums)): 
            sm = 0 
            for end in range(start, len(nums)): 
                sm += nums[end]
                if sm == k: 
                    cnt += 1
        return cnt


# Approach 4: HashMap 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {}
        mp[0] = 1
        sm = 0
        cnt = 0

        for num in nums: 
            sm += num 
            if sm - k in mp: 
                cnt += mp[sm-k] 
            
            mp[sm] = mp.get(sm, 0) + 1
        
        return cnt

