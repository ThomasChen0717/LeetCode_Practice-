# 188. Best Time to Buy and Sell Stock IV

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Array, Dynamic Programming

---

## Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

---

## Examples
**Example 1:** 
```
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

**Example 2:**
```
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```

## Constraints

- `1 <= k <= 100`
- `1 <= prices.length <= 1000`
- `0 <= prices[i] <= 1000`

---

## Approach 1: 3D Dynamic Programming

### Intuition

This problem is a generalization of the "Best Time to Buy and Sell Stock" series. Since we can perform up to `k` transactions, we need to track not only the day and whether we are holding a stock, but also how many transactions we've completed.

This leads to a 3D DP state: `dp[i][j][s]`, representing the maximum profit on day `i`, having completed `j` transactions, and being in state `s` (where `s=0` means we are not holding a stock, and `s=1` means we are).

The state transitions are as follows:
-   `dp[i][j][0]` (not holding): The max of:
    1.  `dp[i-1][j][0]`: We did nothing from the previous day.
    2.  `dp[i-1][j][1] + prices[i]`: We were holding a stock and sold it today.
-   `dp[i][j][1]` (holding): The max of:
    1.  `dp[i-1][j][1]`: We did nothing from the previous day.
    2.  `dp[i-1][j-1][0] - prices[i]`: We were not holding a stock, had completed `j-1` transactions, and bought one today. This starts the `j`-th transaction.

The final answer is `dp[n-1][k][0]`, which is the max profit after `n-1` days, `k` transactions, and not holding any stock.

### Complexity Analysis

-   **Time Complexity:** `O(N * K)`, where `N` is the number of prices and `K` is the number of transactions. We have three nested loops for days, transactions, and states.
-   **Space Complexity:** `O(N * K)` for the 3D DP table.

---

## Approach 2: 1D Dynamic Programming (Space Optimized)

### Intuition

We can optimize the space complexity of the previous approach. Notice that the calculation for day `i` only depends on the results from day `i-1`. This suggests we can reduce the DP table's dimension.

This approach uses two 1D arrays, `profit` and `cost`, of size `k+1`.
-   `profit[i]`: The maximum profit after completing `i` transactions (i.e., after the `i`-th sell).
-   `cost[i]`: The minimum cost to make the `i`-th buy.

We iterate through each `price` in the `prices` array. For each price, we iterate from `i = 1` to `k` to update the costs and profits:
1.  `cost[i] = min(cost[i], price - profit[i-1])`: The cost of the `i`-th buy is the minimum of its current value and the effective cost of buying today. The effective cost is today's `price` minus the profit we made from the previous `i-1` transactions.
2.  `profit[i] = max(profit[i], price - cost[i])`: The profit of the `i`-th sell is the maximum of its current value and the profit from selling today, which is today's `price` minus the cost of the `i`-th buy.

After iterating through all prices, `profit[k]` will contain the maximum profit from at most `k` transactions.

### Complexity Analysis

-   **Time Complexity:** `O(N * K)`. We have nested loops iterating through prices and transactions.
-   **Space Complexity:** `O(K)`. We use two arrays of size `k+1` to store the costs and profits for each transaction number.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
