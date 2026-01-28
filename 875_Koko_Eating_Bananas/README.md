# 875. Koko Eating Bananas

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Binary Search

---

## Problem Description
Koko loves to eat bananas. There are `n` piles of bananas, the ith pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours. 

---

## Examples
Example 1:
```
Input: piles = [3,6,7,11], h = 8
Output: 4
```
Example 2:
```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```
Example 3:
```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

---

## Approach 1: Brute Force

### Intuition

We simply iterate over all possible speeds from 1 to the maximum number of bananas in a pile. For each speed, we calculate the total hours needed to eat all the bananas. If the total hours is less than or equal to `h`, we return the speed. Otherwise, we increment the speed by 1 and repeat the process.

### Complexity Analysis
Let `N` be the number of piles and `M` be the maximum number of bananas in a pile.
- **Time Complexity:** `O(M * N)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Binary Search

### Intuition

We can use binary search to find the minimum speed. We set the left boundary to 1 and the right boundary to the maximum number of bananas in a pile. For each midpoint, we check if Koko can eat all the bananas within `h` hours. If so, we update the right boundary to mid. Otherwise, we update the left boundary to mid + 1.

### Complexity Analysis
- **Time Complexity:** `O(N * log(M))` 
    - Binary Search runs `log(M)` times.
    - For each iteration, we need to check if Koko can eat all the bananas within `h` hours. This takes `O(N)` time. 
    - Also, finding the maximum number of bananas in a pile takes `O(N)` time.
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
