# Coin Change II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Dynamic Programming

---

## Problem Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.

---

## Examples
Example 1:
```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

Example 2:
```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```
Example 3:
```
Input: amount = 10, coins = [10]
Output: 1
```

## Constraints

- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- All the values of coins are **unique**.
- `0 <= amount <= 5000`

---

## Approach 1: Top-Down Dynamic Programming

### Intuition

For a specific coin, we have two options: either we take this coin and decrease the remaining amount we still need, or we ignore the coin and move to the next one without changing the remaining amount we still need. We add the number of ways to make up the required amount from both choices. 

As we may notice, we are breaking down a larger problem into smaller but similar problems, and adding the results of them to get the answer to the original problem.

### Complexity Analysis
Let `n` be the number of coins, and `amount` be the required amount.
- **Time Complexity:** `O(amount * n)`
- **Space Complexity:** `O(amount * n)`

---

## Approach 2: Bottom-Up Dynamic Programming

### Intuition

We can also solve this problem using bottom-up dynamic programming. We create a 2D array `dp` where `dp[i][j]` represents the number of combinations to make up the amount `j` using the first `i` coins.

We initialize `dp[0][0]` to `1`, as there is exactly one way to make up the amount `0` using no coins.

For each coin `coins[i]`, we update `dp[i][j]` as follows:
- If `j < coins[i]`, then `dp[i][j] = dp[i-1][j]`, as we cannot use the current coin.
- If `j >= coins[i]`, then `dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]`, as we have two options: either we use the current coin or we don't.

### Complexity Analysis
- **Time Complexity:** `O(amount * n)`
- **Space Complexity:** `O(amount * n)`

---

## Approach 3: Space-Optimized Dynamic Programming

### Intuition

We notice that we only need the results of the previous coin to update the current one. Therefore, we can optimize the space complexity to `O(amount)`.

### Complexity Analysis
- **Time Complexity:** `O(amount * n)`
- **Space Complexity:** `O(amount)`

---

## Implementation

See `solution.py` for the full implementation.
