# Leaderboard Stats - Average Time per Challenge

## Problem

Given:

* Total time spent in format `H:MM:SS`
* Number of challenges completed

Convert total time into seconds and compute the **average time per challenge**.

## Approach

1. Split the time string into hours, minutes, and seconds.
2. Convert everything into total seconds.
3. Divide by number of challenges.
4. Round to nearest second.

## Solution

```python
def average_time(total, completed):
    h, m, s = map(int, total.split(":"))
    total_seconds = h * 3600 + m * 60 + s
    return round(total_seconds / completed)
```

## Complexity

* Time: O(1)
* Space: O(1)

## Example

Input:
total = "1:41:29", completed = 26

Output:
234
