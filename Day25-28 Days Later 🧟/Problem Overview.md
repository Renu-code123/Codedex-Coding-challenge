# 28 Days Later - Grid Infection Problem

## Problem
Given a 2D grid representing a city:
- ' ' → empty cell  
- '👤' → healthy person  
- '🧟' → infected person  

Each day, infected people spread the virus to adjacent healthy people (up, down, left, right).

Return:
- Minimum number of days required to infect all people  
- `-1` if some people cannot be infected  

---

## Approach
- Use **Breadth-First Search (BFS)**  
- Treat all infected cells as starting points (multi-source BFS)  
- Spread infection level by level (each level = one day)  
- Track remaining healthy people  

---

## Algorithm
1. Count healthy people and store all infected positions in a queue  
2. Perform BFS:
   - For each level, infect adjacent healthy cells  
   - Decrease healthy count  
3. Increment days after each level  
4. If all healthy are infected → return days - 1  
5. Else → return -1  

---

## Code (Python)

```python
from collections import deque

def days_to_infect(city):
    rows, cols = len(city), len(city[0])
    queue = deque()
    healthy = 0

    for r in range(rows):
        for c in range(cols):
            if city[r][c] == '🧟':
                queue.append((r, c))
            elif city[r][c] == '👤':
                healthy += 1

    if healthy == 0:
        return 0

    days = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and city[nr][nc] == '👤':
                    city[nr][nc] = '🧟'
                    healthy -= 1
                    queue.append((nr, nc))

        days += 1

    return days - 1 if healthy == 0 else -1
