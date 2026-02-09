# 155. Min Stack

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Stack, Design

---

## Problem Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element val onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

---

## Examples
Example 1:
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

---

## Approach 1: Stack with pair (num, min)

### Intuition

We can use a stack to store pairs of `(num, min)` where `num` is the number and `min` is the minimum number in the stack up to that point. 

### Complexity Analysis

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Two Stacks

### Intuition

We can use two stacks to store the numbers and the minimum numbers. The first stack will store the numbers and the second stack will store the minimum numbers.

### Complexity Analysis

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Two Stacks with number of duplicates

### Intuition

We can use two stacks to store the numbers and the minimum numbers. The first stack will store the numbers and the second stack will store the number of duplicates of the minimum number in the stack up to that point. 

### Complexity Analysis

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
