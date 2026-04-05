# 657. Robot Return to Origin

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** String, Simulation

---

## Problem Description

There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string `moves` that represents the move sequence of the robot where `moves[i]` represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return `true` if the robot returns to the origin after it finishes all of its moves, or `false` otherwise.

---

## Examples

**Example 1:**
```
Input: moves = "UD"
Output: true
```
**Explanation:** The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

**Example 2:**
```
Input: moves = "LL"
Output: false
```
**Explanation:** The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

## Constraints

- `1 <= moves.length <= 2 * 10^4`
- `moves` only contains the characters 'U', 'D', 'L' and 'R'.

---

## Approach

### Intuition

The problem asks us to determine if a robot, starting at the origin (0,0) on a 2D plane, returns to the origin after a series of moves. The moves are given as a string, and they can be 'U' (up), 'D' (down), 'L' (left), or 'R' (right).

To solve this, we can track the robot's position using two variables: one for the horizontal displacement (`x`) and one for the vertical displacement (`y`). We initialize both `x` and `y` to 0. Then, we iterate through the `moves` string and update the `x` and `y` coordinates based on the move:
- 'U': Increment `y`.
- 'D': Decrement `y`.
- 'R': Increment `x`.
- 'L': Decrement `x`.

After iterating through all the moves, we check if the robot is back at the origin. This will be true if and only if both the horizontal and vertical displacements are zero (`x == 0` and `y == 0`).

An early optimization we can make is to check if the length of the `moves` string is odd. If it is, the robot can never return to the origin, because each move and its opposite cancel each other out, so a return to origin requires an even number of moves.

### Complexity Analysis

- **Time Complexity:** `O(N)`, where `N` is the length of the `moves` string. We iterate through the string once.
- **Space Complexity:** `O(1)`. We only use a few variables to store the horizontal and vertical counts, which is constant extra space.

---

## Implementation

See `solution.py` for the full implementation.
