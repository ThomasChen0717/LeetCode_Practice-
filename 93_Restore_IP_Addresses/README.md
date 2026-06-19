# 93. Restore IP Addresses

**Difficulty:** <span style="color:#f1c40f"><b>Medium</b></span>  
**Topics:** String, Backtracking

---

## Problem Description

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

- For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return _all possible valid IP addresses that can be formed by inserting dots into_ `s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

---

## Examples
**Example 1:**
```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

**Example 2:**
```
Input: s = "0000"
Output: ["0.0.0.0"]
```

**Example 3:**
```
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

## Constraints

- `1 <= s.length <= 20`
- `s` consists of digits only.

---

## Approach 1: Backtracking

### Intuition

This problem can be solved by exploring all possible ways to place three dots in the string to form four segments. This is a classic backtracking problem.

We can define a recursive helper function that builds the IP address segment by segment. The function would need to keep track of the current position in the string and how many segments we have already formed.

At each step, we can try to form a new segment of length 1, 2, or 3. For each potential segment, we must validate it:
1. The segment's value must be between 0 and 255.
2. The segment cannot have a leading zero unless it is the number 0 itself.

If the segment is valid, we recursively call the function for the rest of the string. When we have successfully formed four segments and consumed the entire string, we have found a valid IP address.

To optimize, we can add pruning conditions. For instance, if the remaining string is too long or too short to form the remaining segments, we can stop exploring that path.

### Complexity Analysis

- **Time Complexity:** `O(1)`. The maximum length of a valid IP address string is 12 (`255.255.255.255`). The problem statement gives a maximum length of 20 for `s`, but any string with a length greater than 12 can't form a valid IP address. The number of ways to place 3 dots is bounded, so the number of recursive calls is limited, making the complexity constant.
- **Space Complexity:** `O(1)`. The recursion depth is at most 4. The space used by the recursion stack and the temporary variables is constant.

---

## Approach 2: Iteration

### Intuition

Instead of recursion, we can use nested loops to generate all possible combinations of segment lengths.

Since an IP address has four segments, we can use three nested loops to determine the lengths of the first three segments. The length of the fourth segment will be the remaining length of the string.

Each of the first three segments can have a length of 1, 2, or 3. We can iterate through these possibilities:
- The outer loop iterates through possible lengths for the first segment.
- The second loop iterates through possible lengths for the second segment.
- The third loop iterates through possible lengths for the third segment.

For each combination of lengths, we check if all four resulting segments are valid (using the same validation logic as in the backtracking approach). If they are, we construct the IP address string and add it to our result list.

This approach avoids recursion and can be more efficient in some cases, as it eliminates the overhead of function calls.

### Complexity Analysis

- **Time Complexity:** `O(1)`. We have three nested loops, each running at most 3 times (for segment lengths 1, 2, and 3). This gives a constant number of iterations (3*3*3 = 27). The work done inside the loops is also constant time.
- **Space Complexity:** `O(1)`. We only use a few variables to store the segment lengths and the resulting IP addresses. The space required is constant, excluding the storage for the final answer.

---

## Implementation

See `solution.c++` for the full implementation of both approaches.