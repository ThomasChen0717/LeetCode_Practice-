# 123. Best Time to Buy and Sell Stock III

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Array, Dynamic Programming

---

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

---

## Examples
**Example 1:** 
```
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

**Example 2:**
```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging in multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^5`

---

## Approach 1: Bidirectional Dynamic Programming

### Intuition

The core idea is that the two transactions can be split by any given day. If we make a split at day `i`, we have two independent subproblems: finding the max profit from one transaction in `prices[0...i]` and finding the max profit from one transaction in `prices[i+1...n-1]`.

We can pre-compute these values:
1.  `left_profits`: An array where `left_profits[i]` stores the maximum profit from one transaction in the subarray `prices[0...i]`.
2.  `right_profits`: An array where `right_profits[i]` stores the maximum profit from one transaction in the subarray `prices[i...n-1]`.

`left_profits` is built by iterating from left to right, keeping track of the minimum price seen so far. `right_profits` is built by iterating from right to left, keeping track of the maximum price seen so far.

Finally, we can iterate from `i = 0` to `n-1` and find the maximum of `left_profits[i] + right_profits[i+1]`. This sum represents the total profit if we complete the first transaction by day `i` and start the second transaction on or after day `i+1`.

### Complexity Analysis

-   **Time Complexity:** `O(N)`, where `N` is the length of `prices`. We perform a few separate passes over the array, each taking `O(N)` time.
-   **Space Complexity:** `O(N)` to store the `left_profits` and `right_profits` arrays.

---

## Approach 2: One-Pass State Machine

### Intuition

This is a highly optimized approach that solves the problem in a single pass. We can think of the process as a state machine with four states representing the maximum profit at each stage of two transactions:

-   `t1_cost`: The minimum cost of buying the first stock.
-   `t1_profit`: The maximum profit after selling the first stock.
-   `t2_cost`: The minimum cost of buying the second stock, considering the profit from the first.
-   `t2_profit`: The maximum profit after selling the second stock.

We iterate through the prices and update these four variables:
1.  `t1_cost`: The cost of the first buy is the minimum of the current `t1_cost` and the current `price`.
2.  `t1_profit`: The profit from the first sell is the maximum of the current `t1_profit` and `price - t1_cost`.
3.  `t2_cost`: The effective cost of the second buy is `price - t1_profit`. We want to minimize this cost.
4.  `t2_profit`: The profit from the second sell is the maximum of the current `t2_profit` and `price - t2_cost`.

After iterating through all prices, `t2_profit` will hold the maximum profit achievable from at most two transactions. This works because if only one transaction is optimal, `t2_profit` will end up being equal to `t1_profit`.

### Complexity Analysis

-   **Time Complexity:** `O(N)`. We iterate through the `prices` array only once.
-   **Space Complexity:** `O(1)`. We only use a few variables to track the costs and profits.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
