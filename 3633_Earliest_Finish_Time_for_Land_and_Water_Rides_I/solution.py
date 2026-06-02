# Approach 1: Brute Force
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime) 
        res = float('inf')

        for i in range(n): 
            for j in range(m): 
                land = landStartTime[i] + landDuration[i]
                land_water = max(land, waterStartTime[j]) + waterDuration[j] 
                res = min(res, land_water) 


                water = waterStartTime[j] + waterDuration[j]
                water_land = max(water, landStartTime[i]) + landDuration[i] 
                res = min(res, water_land) 

        return res 

# Approach 2: Linear Enumeration
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:        
        def solve(startTime1, duration1, startTime2, duration2): 
            finish1 = float('inf')
            for i in range(len(startTime1)): 
                finish1 = min(finish1, startTime1[i] + duration1[i]) 
            
            finish2 = float('inf')
            for j in range(len(startTime2)): 
                finish2 = min(finish2, max(finish1, startTime2[j]) + duration2[j])

            return finish2

        land_water = solve(landStartTime, landDuration, waterStartTime, waterDuration) 
        water_land = solve(waterStartTime, waterDuration, landStartTime, landDuration)
            
        return min(land_water, water_land)


        