class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0 
        mp = {}
        curr_sum = 0 

        for i in range(len(nums)): 
            curr_sum += 1 if nums[i] == 1 else -1 

            if curr_sum == 0: 
                max_len = max(max_len, i + 1)
            if curr_sum in mp: 
                max_len = max(max_len, i - mp[curr_sum])
            else: 
                mp[curr_sum] = i 

        return max_len 



            


