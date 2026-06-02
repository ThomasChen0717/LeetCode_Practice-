# 3633. Earliest Finish Time for Land and Water Rides I

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Array, Greedy

---

## Problem Description

You are given two categories of theme park attractions: **land rides** and **water rides**.

- **Land rides**
  - `landStartTime[i]` – the earliest time the `i`th land ride can be boarded.
  - `landDuration[i]` – how long the `i`th land ride lasts.
- **Water rides**
  - `waterStartTime[j]` – the earliest time the `j`th water ride can be boarded.
  - `waterDuration[j]` – how long the `j`th water ride lasts.

A tourist must experience **exactly one** ride from **each** category, in **either order**.

- A ride may be started at its opening time or **any later moment**.
- If a ride is started at time `t`, it finishes at time `t + duration`.
- Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the **earliest possible time** at which the tourist can finish both rides.

---

## Examples

**Example 1:**
```
Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
Output: 9
```
**Explanation:**
- Plan A (land ride 0 → water ride 0):
  - Start land ride 0 at time `landStartTime[0] = 2`. Finish at `2 + landDuration[0] = 6`.
  - Water ride 0 opens at time `waterStartTime[0] = 6`. Start immediately at `6`, finish at `6 + waterDuration[0] = 9`.
- Plan B (water ride 0 → land ride 1):
  - Start water ride 0 at time `waterStartTime[0] = 6`. Finish at `6 + waterDuration[0] = 9`.
  - Land ride 1 opens at `landStartTime[1] = 8`. Start at time `9`, finish at `9 + landDuration[1] = 10`.

Plan A gives the earliest finish time of 9.

**Example 2:**
```
Input: landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]
Output: 14
```
**Explanation:**
- Plan A (water ride 0 → land ride 0):
  - Start water ride 0 at time `waterStartTime[0] = 1`. Finish at `1 + waterDuration[0] = 11`.
  - Land ride 0 opened at `landStartTime[0] = 5`. Start immediately at `11` and finish at `11 + landDuration[0] = 14`.
- Plan B (land ride 0 → water ride 0):
  - Start land ride 0 at time `landStartTime[0] = 5`. Finish at `5 + landDuration[0] = 8`.
  - Water ride 0 opened at `waterStartTime[0] = 1`. Start immediately at `8` and finish at `8 + waterDuration[0] = 18`.

Plan A provides the earliest finish time of 14.

## Constraints

- `1 <= n, m <= 100`
- `landStartTime.length == landDuration.length == n`
- `waterStartTime.length == waterDuration.length == m`
- `1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000`

---

## Approach 1: Brute Force

### Intuition

The problem requires us to find the earliest finish time by choosing one land ride and one water ride. Since we can choose any pair of rides and do them in any order, a brute-force approach is to check every single possibility.

We can iterate through each land ride `i` and each water ride `j`. For each pair `(i, j)`, we calculate the total time for two possible scenarios:
1.  **Land ride first, then water ride:**
    - Finish time of land ride `i`: `landStartTime[i] + landDuration[i]`.
    - Start time of water ride `j`: `max(finish time of land ride, waterStartTime[j])`.
    - Final finish time: `start time of water ride + waterDuration[j]`.
2.  **Water ride first, then land ride:**
    - Finish time of water ride `j`: `waterStartTime[j] + waterDuration[j]`.
    - Start time of land ride `i`: `max(finish time of water ride, landStartTime[i])`.
    - Final finish time: `start time of land ride + landDuration[i]`.

We keep track of the minimum finish time found across all pairs and both orderings. This guarantees we find the global minimum.

### Complexity Analysis

- **Time Complexity:** `O(N * M)`, where `N` is the number of land rides and `M` is the number of water rides. We have nested loops iterating through all pairs.
- **Space Complexity:** `O(1)`.

---

## Approach 2: Linear Enumeration (Greedy)

### Intuition

The brute-force approach is correct but can be optimized. Notice that for a fixed order (e.g., land then water), the choice of the second ride depends on when the *first* ride finishes. To get the earliest possible final finish time, we should aim to finish the first ride as early as possible.

This leads to a greedy strategy:
1.  **Consider the Land-then-Water order:**
    - First, find the earliest possible time to finish *any* land ride. This would be `min(landStartTime[i] + landDuration[i])` over all land rides `i`. Let's call this `earliest_land_finish`.
    - Now, with this `earliest_land_finish` time, iterate through all water rides `j`. For each water ride, the earliest we can finish is `max(earliest_land_finish, waterStartTime[j]) + waterDuration[j]`.
    - Find the minimum of these times over all water rides `j`.

2.  **Consider the Water-then-Land order:**
    - Similarly, find the `earliest_water_finish` by taking `min(waterStartTime[j] + waterDuration[j])` over all water rides `j`.
    - Then, for each land ride `i`, calculate the finish time `max(earliest_water_finish, landStartTime[i]) + landDuration[i]`.
    - Find the minimum of these times over all land rides `i`.

3.  **Final Result:** The answer is the minimum of the results from step 1 and step 2.

This approach avoids the nested `N*M` loop by breaking the problem down. Instead of pairing every ride, we find the best-case scenario for the first leg of the journey and then find the best second leg based on that.

### Complexity Analysis

- **Time Complexity:** `O(N + M)`. We make two passes through the land rides and two passes through the water rides.
- **Space Complexity:** `O(1)`.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
