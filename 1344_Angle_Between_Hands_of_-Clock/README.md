# 1344. Angle Between Hands of a Clock

**Difficulty:** <span style="color:#f1c40f"><b>Medium</b></span>  
**Topics:** Math

---

## Problem Description

Given two numbers, `hour` and `minutes`, return *the smaller angle (in degrees) formed between the* `hour` *and the* `minute` *hand*.

---

## Examples
Example 1: 
```
Input: hour = 12, minutes = 30
Output: 165
```
Example 2:
```
Input: hour = 3, minutes = 30
Output: 75
```
Example 3:
```
Input: hour = 3, minutes = 15
Output: 7.5
```

## Constraints

- `1 <= hour <= 12`
- `0 <= minutes <= 59`

---

## Approach

### Intuition

The problem is to find the smaller angle between the hour and minute hands of a clock.

The position of the minute hand is straightforward to calculate. There are 60 minutes in an hour, and a full circle is 360 degrees. So, the minute hand moves `360 / 60 = 6` degrees per minute. The position of the minute hand is `minutes * 6`.

The position of the hour hand is slightly trickier. The hour hand moves 360 degrees in 12 hours. So, it moves `360 / 12 = 30` degrees per hour. However, the position of the hour hand is also affected by the minutes. For example, at 3:30, the hour hand is halfway between 3 and 4. The hour hand moves `30 / 60 = 0.5` degrees per minute. So, the position of the hour hand is `(hour % 12 + minutes / 60.0) * 30`. The modulo 12 is to handle the case where the hour is 12.

Once we have the angles of the hour and minute hands, we can find the absolute difference between them. This gives us one angle. The other angle is `360 - angle`. We need to return the smaller of these two angles.

### Complexity Analysis

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.c++` for the full implementation.