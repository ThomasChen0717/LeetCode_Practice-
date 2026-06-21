# 1833. Maximum Ice Cream Bars

**Difficulty:** <span style="color:#f1c40f"><b>Medium</b></span>  
**Topics:** Array, Sorting, Greedy

---

## Problem Description

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the price of the `i`th ice cream bar in coins. The boy initially has `coins` coins to spend, and he wants to buy as many ice cream bars as possible.

Return _the **maximum** number of ice cream bars the boy can buy with_ `coins` _coins._

**Note:** The boy can buy the ice cream bars in any order.

---

## Examples

**Example 1:**
```
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
```

**Example 2:**
```
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.
```

**Example 3:**
```
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
```

## Constraints

- `costs.length == n`
- `1 <= n <= 10^5`
- `1 <= costs[i] <= 10^5`
- `1 <= coins <= 10^8`

---

## Approach: Counting Sort

### Intuition

To maximize the number of ice cream bars, it's always best to buy the cheapest ones first. This suggests a greedy approach. We could sort the `costs` array and iterate through it, buying ice cream bars until we run out of coins. However, a standard `O(n log n)` sort might be too slow given the constraints.

Since the costs are within a reasonable range, we can use a more efficient sorting method like counting sort, which has a linear time complexity.

The idea is to count the frequency of each cost and then iterate through the costs from smallest to largest. For each cost, we buy as many ice cream bars as we can afford.

### Algorithm

1.  **Create a frequency map (or an array for counting sort):** We can use an array, say `costsFrequency`, to store the number of ice cream bars for each cost. The size of this array will be `max(costs) + 1` or, in this case, we can cap it at `coins + 1` since we can't buy any ice cream that costs more than the total coins we have.

2.  **Populate the frequency map:** Iterate through the `costs` array. For each `cost`, if it's within our `coins` limit, increment `costsFrequency[cost]`.

3.  **Iterate and buy:** Iterate from `cost = 1` up to `coins`. For each cost:
    - If we can't afford even one ice cream of the current cost (`currentCoins < cost`), we can break the loop since all subsequent costs will be higher.
    - Determine how many ice cream bars of the current cost we can buy. This will be the minimum of the number of available bars (`costsFrequency[cost]`) and the number we can afford (`currentCoins / cost`).
    - Add this number to our total count of ice cream bars.
    - Subtract the total price of the purchased bars from `currentCoins`.

4.  **Return the total count.**

### Complexity Analysis

-   **Time Complexity:** `O(n + coins)`, where `n` is the number of ice cream bars and `coins` is the total money. `O(n)` to build the frequency map, and `O(coins)` to iterate through possible costs. This is more efficient than `O(n log n)` when `coins` is not excessively large compared to `n log n`.
-   **Space Complexity:** `O(coins)` for the frequency map.

---

## Implementation

See `solution.c++` for the full implementation.
