# Infinite Monkey Theorem

A Python solution using the sliding window technique to find the most similar substring between a target and an attempt string.

## Problem

Given two strings:
- `target`
- `attempt` (longer string)

Return:
- `best_index`: starting index of best match
- `similarity`: match percentage
- `attempts`: estimated attempts to reach 100% match (or null if 0%)

## Approach

- Slide a window of size `len(target)` over `attempt`
- Count position-wise matches
- Compute similarity:
  similarity = (matches / len(target)) * 100
- Track maximum similarity and index
- Estimate attempts:
  attempts = (100 / similarity) ** len(target)

## Code

```python
def infinite_monkey(target, attempt):
    n = len(target)
    best_similarity = 0
    best_index = 0

    for i in range(len(attempt) - n + 1):
        matches = sum(1 for j in range(n) if attempt[i+j] == target[j])
        similarity = (matches / n) * 100

        if similarity > best_similarity:
            best_similarity = similarity
            best_index = i

    attempts = None if best_similarity == 0 else round((100 / best_similarity) ** n)

    return {
        'best_index': best_index,
        'similarity': round(best_similarity, 2),
        'attempts': attempts
    }
```
