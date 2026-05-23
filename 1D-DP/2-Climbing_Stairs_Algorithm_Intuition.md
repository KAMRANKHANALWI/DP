## Climbing Stairs — Algorithm & Intuition

**Problem:** You have `n` stairs. From any stair you can take 1 or 2 steps. How many **distinct ways** can you reach the top?

```
n=1 → [1]                       = 1 way
n=2 → [1,1] or [2]              = 2 ways
n=3 → [1,1,1], [1,2], [2,1]    = 3 ways
n=4 → [1,1,1,1],[1,1,2],[1,2,1],[2,1,1],[2,2] = 5 ways
```

---

### Intuition

**The Dream:** Count every path to the top.

**Key Insight:** To reach stair `n`, you either came from stair `n-1` (took 1 step) or from stair `n-2` (took 2 steps). So:

```
ways(n) = ways(n-1) + ways(n-2)
```

This is exactly the Fibonacci recurrence — but with different base cases.

```
Fibonacci:      fib(0)=0, fib(1)=1
Climbing Stairs: ways(0)=1, ways(1)=1

ways(0) = 1  ← standing at ground, 1 way to "be at the top" (do nothing)
ways(1) = 1  ← only one step possible
ways(2) = 2  ← [1,1] or [2]
ways(3) = 3  ← ways(2) + ways(1) = 2+1 = 3
ways(4) = 5  ← ways(3) + ways(2) = 3+2 = 5
```

---

### Why `ways(n) = ways(n-1) + ways(n-2)`?

```
To land on stair n:
  Last step was 1 → came from stair n-1 → ways(n-1) paths led here
  Last step was 2 → came from stair n-2 → ways(n-2) paths led here

No other option (can only take 1 or 2 steps).
Total = ways(n-1) + ways(n-2)
```

---

### Dry Run — n=5

```
Memoization:
dp = [-1, -1, -1, -1, -1, -1]

ways(5) → ways(4) + ways(3)
ways(4) → ways(3) + ways(2)
ways(3) → ways(2) + ways(1)
ways(2) → ways(1) + ways(0) = 1+1 = 2  → dp[2]=2
ways(3) = 2+1 = 3  → dp[3]=3
ways(4) = 3+2 = 5  → dp[4]=5
ways(5) = 5+3 = 8  → dp[5]=8 ✅
```

```
Tabulation:
dp = [1, 1, -, -, -, -]

i=2: dp[2] = dp[1]+dp[0] = 2
i=3: dp[3] = dp[2]+dp[1] = 3
i=4: dp[4] = dp[3]+dp[2] = 5
i=5: dp[5] = dp[4]+dp[3] = 8 ✅
```

```
Space Optimized:
prev2=1, prev=1

i=2: curi=1+1=2  → prev2=1, prev=2
i=3: curi=1+2=3  → prev2=2, prev=3
i=4: curi=2+3=5  → prev2=3, prev=5
i=5: curi=3+5=8  → prev=8 ✅
```

---

### Climbing Stairs vs Fibonacci

```
Feature         | Fibonacci       | Climbing Stairs
----------------|-----------------|----------------
Recurrence      | f(n-1)+f(n-2)   | f(n-1)+f(n-2)   ← identical
Base: index 0   | fib(0) = 0      | ways(0) = 1
Base: index 1   | fib(1) = 1      | ways(1) = 1
Interpretation  | count value     | count paths
```

The only difference is `dp[0]=1` instead of `dp[0]=0`. The rest is the same code.

---

### Generalisation

If you could take 1, 2, or 3 steps:
```
ways(n) = ways(n-1) + ways(n-2) + ways(n-3)
```
→ Tribonacci. Frog Jump K-distance generalises this to `k` steps.

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N) | O(N) |
| Tabulation | O(N) | O(N) |
| Space Optimized | O(N) | O(1) |
