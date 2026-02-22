# Approach 1: Brute Force Optimized
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits) 

        cnt = 0

        for i in range(n): 
            unique_st = set() 
            for j in range(i, n):
                if fruits[j] not in unique_st and len(unique_st) == 2: 
                    break 
                
                unique_st.add(fruits[j]) 
                cnt = max(cnt, j - i + 1)
        
        return cnt

# Approach 2: Sliding Window
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits) 

        cnt = 0

        left = 0 

        unique_mp = collections.defaultdict(int) 


        for right in range(n):  
            curr_fruit = fruits[right] 

            unique_mp[curr_fruit] += 1

            while len(unique_mp) > 2: 
                left_fruit = fruits[left] 
                unique_mp[left_fruit] -= 1
                
                if unique_mp[left_fruit] == 0: del unique_mp[left_fruit]

                left += 1
                
            cnt = max(cnt, right - left + 1)
        
        return cnt