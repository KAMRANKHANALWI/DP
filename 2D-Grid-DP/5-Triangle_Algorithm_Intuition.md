## Triangle — Algorithm & Intuition

**Problem:** Given a triangular array, find the **minimum path sum from top to bottom**. At each row `i`, from position `j` you can move to `j` or `j+1` in row `i+1`.

```
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

     2
    3 4
   6 5 7
  4 1 8 3

→ minimum path sum = 11  (2 → 3 → 5 → 1)
```

---

### Intuition

**The Dream:** Walk from the tip to the base spending as little as possible.

**Key Insight:** From cell `(i, j)` you can only go to `(i+1, j)` (straight down) or `(i+1, j+1)` (diagonal right). Work **bottom-up** — at each cell, take the cheaper of the two paths below you.

```
dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
```

Bottom-up is cleaner here: the last row is the base case (no choice below), and you build upward to `dp[0][0]`.

---

### Why Bottom-Up (Not Top-Down)?

```
Top-down issue: variable number of destinations
  From (0,0): can go to (1,0) or (1,1)
  Need to take min of two sub-paths that grow downward

Bottom-up advantage: last row is trivially the base case
  dp[n-1][j] = triangle[n-1][j]   ← no choice, just the value
  Then fill upward — each cell just looks at two already-computed cells below it
```

---

### Dry Run — `[[2],[3,4],[6,5,7],[4,1,8,3]]`

```
n=4

Copy last row as base:
dp[3] = [4, 1, 8, 3]

Row i=2:  (dp[2][j] = triangle[2][j] + min(dp[3][j], dp[3][j+1]))
  j=0: 6 + min(4,1) = 6+1 = 7
  j=1: 5 + min(1,8) = 5+1 = 6
  j=2: 7 + min(8,3) = 7+3 = 10
dp[2] = [7, 6, 10, _]

Row i=1:
  j=0: 3 + min(7,6) = 3+6 = 9
  j=1: 4 + min(6,10)= 4+6 = 10
dp[1] = [9, 10, _, _]

Row i=0:
  j=0: 2 + min(9,10) = 2+9 = 11
dp[0] = [11, _, _, _]

Answer = dp[0][0] = 11 ✅
Path: 2→3→5→1 = 11
```

---

### Space Optimization — One Row at a Time

```
Keep only the "front" (next row) and compute "curr" (current row).

front = [4, 1, 8, 3]   ← last row

i=2:
  curr = [7, 6, 10]
  front = [7, 6, 10]

i=1:
  curr = [9, 10]
  front = [9, 10]

i=0:
  curr = [11]
  front = [11]

return front[0] = 11 ✅
```

---

### Row Width Matters

```
Row i has exactly (i+1) elements.
  Row 0: 1 element
  Row 1: 2 elements
  ...
  Row n-1: n elements

In the space-optimized version:
  curr = [0] * (i+1)   ← size shrinks as you go up
  for j in range(i+1): ...
```

---

### Top-Down Memoization (Alternative)

```
Go from (0,0) downward:
  triangle_memo(i, j) = triangle[i][j] + min(
      triangle_memo(i+1, j),
      triangle_memo(i+1, j+1)
  )
  Base: i == n-1 → return triangle[n-1][j]

dp[i][j] shaped per row (jagged): [[-1]*len(row) for row in triangle]
```

---

### Recurrence Summary

```
Base: dp[n-1][j] = triangle[n-1][j]

Transition (bottom-up):
  dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
  for j in range(i+1)

Answer = dp[0][0]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N²) | O(N²) |
| Tabulation | O(N²) | O(N²) |
| Space Optimized | O(N²) | O(N) |
