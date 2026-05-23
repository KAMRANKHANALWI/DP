## Minimum Path Sum in Grid — Algorithm & Intuition

**Problem:** Given an `m × n` grid of non-negative numbers, find a path from **top-left to bottom-right** (only right or down moves) that **minimises the sum** of all numbers along the path.

```
grid = [[5, 9, 6],
        [11, 5, 2]]
→ minimum sum = 21
```

---

### Intuition

**The Dream:** Walk from corner to corner spending as little as possible.

**Key Insight:** To reach cell `(i, j)` with minimum cost, you pick the cheaper of the two directions you could have come from — above `(i-1, j)` or left `(i, j-1)` — and add the current cell's cost.

```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

---

### The "Out of Bounds = Infinity" Trick

```
If you can't come from above (i==0), treat that cost as ∞.
If you can't come from the left (j==0), treat that cost as ∞.

Taking min(∞, valid) = valid → naturally picks the only available direction.

No special-casing needed for top row or left column.
```

---

### Dry Run — `[[5,9,6],[11,5,2]]`

```
   j=0   j=1   j=2
i=0 [  5,  14,  20 ]
i=1 [ 16,  19,  21 ]

dp[0][0] = 5                            (start)
dp[0][1] = 9  + min(inf, 5)  = 14      (only from left)
dp[0][2] = 6  + min(inf, 14) = 20      (only from left)
dp[1][0] = 11 + min(5, inf)  = 16      (only from above)
dp[1][1] = 5  + min(14, 16)  = 19      (from above=14 cheaper)
dp[1][2] = 2  + min(20, 19)  = 21      (from left=19 cheaper)

Answer = 21 ✅

Path: (0,0)→(0,1)→(1,1)→(1,2)
Cost:   5 +  9  +  5  +  2  = 21 ✅
```

---

### Recurrence in Each Approach

```
Recursion (top-down):
  min_path(i, j) = grid[i][j] + min(
      min_path(i-1, j),   ← from above
      min_path(i, j-1)    ← from left
  )
  Base: min_path(0,0) = grid[0][0]
  OOB:  return inf

Tabulation (bottom-up):
  Fill row by row, left to right.
  up   = dp[i-1][j] if i>0 else inf
  left = dp[i][j-1] if j>0 else inf
  dp[i][j] = grid[i][j] + min(up, left)
```

---

### Space Optimization

```
Only need the previous row → use a 1D `prev` array.

prev = [inf] * n

Row 0:
  curr[0] = grid[0][0] + min(inf, inf) ... no.

Actually:
  curr[j] = grid[i][j] + min(prev[j], curr[j-1])
  where prev[j] = "from above" and curr[j-1] = "from left"
  both start as inf if not yet filled.

After each row: prev = curr
```

---

### Unique Paths vs Min Path Sum

```
Unique Paths:   dp[i][j] = dp[i-1][j] + dp[i][j-1]   (count, OOB=0)
Min Path Sum:   dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])   (cost, OOB=inf)

Same movement structure. Different operation:
  Counting paths → add.  Minimising cost → min + cell cost.
```

---

### Recurrence Summary

```
dp[0][0] = grid[0][0]

dp[i][j] = grid[i][j] + min(
    dp[i-1][j]  (if i > 0, else ∞),
    dp[i][j-1]  (if j > 0, else ∞)
)

Answer = dp[m-1][n-1]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(M×N) | O(M×N) |
| Tabulation | O(M×N) | O(M×N) |
| Space Optimized | O(M×N) | O(N) |
