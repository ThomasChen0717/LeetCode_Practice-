# Approach 1: Brute Force 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Approach 2: Sorting 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)

# Approach 3: Brute Force with Set 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0 

        for num in nums_set: 
            if num - 1 not in nums_set: 
                curr_streak = 1

                while num + 1 in nums_set: 
                    curr_streak += 1 
                    num = num + 1 
                
                longest_streak = max(curr_streak, longest_streak)
        
        return longest_streak