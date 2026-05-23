## Maximum Falling Path Sum — Algorithm & Intuition

**Problem:** Given an `n × n` matrix, start from **any cell in the first row** and fall to the last row. From cell `(i, j)` you can move to `(i+1, j-1)`, `(i+1, j)`, or `(i+1, j+1)`. Maximise the sum of all cells visited.

```
matrix = [[1,  2, 10,  4],
          [100, 3,  2,  1],
          [1,   1, 20,  2],
          [1,   2,  2,  1]]
→ maximum falling path sum = 105
```

---

### Intuition

**The Dream:** Pick the most profitable column to start and fall through the heaviest cells.

**Key Insight:** Work **top-down** (row 0 to row n-1). At each cell, you arrived from one of three cells in the previous row (up, up-left-diagonal, up-right-diagonal). Track the max sum achievable to each cell. Answer = max of the last row.

```
dp[i][j] = max sum to reach cell (i,j) from row 0

dp[i][j] = matrix[i][j] + max(
    dp[i-1][j],      ← straight up
    dp[i-1][j-1],    ← from left-diagonal (if j > 0, else -inf)
    dp[i-1][j+1]     ← from right-diagonal (if j < m-1, else -inf)
)
```

---

### Variable Start Point

```
Row 0 is the base case: dp[0][j] = matrix[0][j] for all j.
Any column can be the starting point — all are initialised.

Answer = max(dp[n-1])   ← variable ending point too
```

---

### Dry Run — 4×4 Matrix

```
matrix = [[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]

dp[0] = [1, 2, 10, 4]   ← base case

Row 1 (up, up-left, up-right):
  j=0: 100 + max(-inf, -inf, dp[0][0]=1, dp[0][1]=2)
       = 100 + max(dp[0][0], dp[0][1])
       Note: j=0, no j-1. dp[0][-inf treated], dp[0][0]=1, dp[0][1]=2
       = 100 + max(1, 2) = 102      ← from dp[0][1] (right-diagonal)

  Actually let me redo with the three directions properly:
  j=0: up=dp[0][0]=1, left=-inf (j<0), right=dp[0][1]=2
       max=2 → 100+2=102
  j=1: up=dp[0][1]=2, left=dp[0][0]=1, right=dp[0][2]=10
       max=10 → 3+10=13
  j=2: up=dp[0][2]=10, left=dp[0][1]=2, right=dp[0][3]=4
       max=10 → 2+10=12
  j=3: up=dp[0][3]=4, left=dp[0][2]=10, right=-inf
       max=10 → 1+10=11

dp[1] = [102, 13, 12, 11]

Row 2:
  j=0: 1+max(-inf, -inf, 102, 13) = 1+max(102,13)=103  (up=102)
       Wait: up=dp[1][0]=102, left=-inf, right=dp[1][1]=13
       → 1+102 = 103
  j=1: 1+max(dp[1][1]=13, dp[1][0]=102, dp[1][2]=12) = 1+102=103
  j=2: 20+max(dp[1][2]=12, dp[1][1]=13, dp[1][3]=11) = 20+13=33
  j=3: 2+max(dp[1][3]=11, dp[1][2]=12, -inf) = 2+12=14

dp[2] = [103, 103, 33, 14]

Row 3:
  j=0: 1+max(-inf, 103, 103) = 1+103=104
  j=1: 2+max(103, 103, 33) = 2+103=105
  j=2: 2+max(33, 103, 14) = 2+103=105
  j=3: 1+max(14, 33, -inf) = 1+33=34

dp[3] = [104, 105, 105, 34]

Answer = max(dp[3]) = 105 ✅
```

---

### Boundary Handling — `-inf` for Out-of-Bounds

```
At j=0:  no left-diagonal above → treat as -inf
At j=m-1: no right-diagonal above → treat as -inf

Using float('-inf') ensures max() never picks an invalid cell.

Code:
  left_diagonal  = dp[i-1][j-1] if j > 0   else float('-inf')
  right_diagonal = dp[i-1][j+1] if j < m-1 else float('-inf')
```

---

### Space Optimization

```
Only need the previous row.

prev = matrix[0][:]   ← row 0

For i in range(1, n):
    curr = [0] * m
    For j in range(m):
        up    = prev[j]
        left  = prev[j-1] if j>0   else -inf
        right = prev[j+1] if j<m-1 else -inf
        curr[j] = matrix[i][j] + max(up, left, right)
    prev = curr

return max(prev)
```

---

### This vs Triangle vs Min Path Sum

```
Min Path Sum:         fixed start (0,0), fixed end (m-1,n-1)
                      2 directions (right, down)

Triangle:             fixed start (0,0), variable end (last row)
                      2 directions (down, diagonal-right)

Falling Path Sum:     variable start (any col, row 0),
                      variable end (any col, last row)
                      3 directions (down, diag-left, diag-right)
```

Each adds one more degree of freedom — variable start/end, more movement directions.

---

### Recurrence Summary

```
dp[0][j] = matrix[0][j]   for all j   ← base: any start

dp[i][j] = matrix[i][j] + max(
    dp[i-1][j],
    dp[i-1][j-1]  (if j > 0, else -inf),
    dp[i-1][j+1]  (if j < m-1, else -inf)
)

Answer = max(dp[n-1])
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N×M) | O(N×M) |
| Tabulation | O(N×M) | O(N×M) |
| Space Optimized | O(N×M) | O(M) |
