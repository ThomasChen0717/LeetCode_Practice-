# Approach: Hash Table
class Solution:
    def distance(self, i, j, k): 
        return abs(i - j) + abs(j - k) + abs(k - i)


    def minimumDistance(self, nums: List[int]) -> int:
        mp = collections.defaultdict(list) 

        min_dis = float('inf')

        for i, num in enumerate(nums): 
            mp[num].append(i) 
            if len(mp[num]) == 3: 
                i, j, k = mp[num] 
                min_dis = min(min_dis, self.distance(i,j,k)) 

                mp[num].pop(0)

        
        return min_dis if min_dis != float('inf') else -1

