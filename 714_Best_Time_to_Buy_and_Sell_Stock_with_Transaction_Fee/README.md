# 714. Best Time to Buy and Sell Stock with Transaction Fee

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming

---

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**Note:**

- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- The transaction fee is only charged once for each stock purchase and sale.

---

## Examples
Example 1:
```
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```
Example 2:
```
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
```
## Constraints

- `1 <= prices.length <= 5 * 10^4`
- `1 <= prices[i] < 5 * 10^4`
- `0 <= fee < 5 * 10^4`

---

## Approach 1: Dynamic Programming

### Intuition

We impose the transaction fee on sell action. Then we can use dynamic programming with two arrays, hold and sell.
- hold[i]: the maximum profit we can have if we hold the stock on day i
- sell[i]: the maximum profit we can have if we sell the stock on day i

The update rule is intuitive, 
- hold[i] = max(hold[i-1], sell[i-1] - prices[i])
    - either we hold the stock from day i-1, or we do not hold a stock on day i-1, and buy the stock on day i
- sell[i] = max(sell[i-1], hold[i-1] + prices[i] - fee)
    - either we keep the profit from selling the stock from day i-1, or we hold a stock on day i-1, and sell the stock on day i

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Space Optimization

### Intuition

We can optimize the space complexity to `O(1)` by using two variables instead of two arrays.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
