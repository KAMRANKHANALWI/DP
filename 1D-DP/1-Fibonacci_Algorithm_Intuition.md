## Fibonacci — Algorithm & Intuition

**Problem:** Find the `n`th Fibonacci number where `fib(0)=0`, `fib(1)=1`, and `fib(n) = fib(n-1) + fib(n-2)`.

```
fib(0)=0, fib(1)=1, fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5 ...
```

This is the **gateway problem** of Dynamic Programming — simple enough to understand, rich enough to demonstrate all three DP techniques.

---

### Why Naive Recursion Fails

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2) ← computed again
│   │   └── fib(1)
│   └── fib(2)     ← computed again
└── fib(3)         ← computed again
    ├── fib(2)     ← computed again
    └── fib(1)
```

`fib(2)` is computed 3 times, `fib(3)` twice. Time = O(2^N) — exponential blowup from **overlapping subproblems**.

---

### Approach 1 — Memoization (Top-Down DP)

**Idea:** Recurse like before, but cache results. If `dp[n] != -1`, return it instantly.

```
dp = [-1, -1, -1, -1, -1, -1]   ← n=5

fib(5): dp[5]=-1 → compute
  fib(4): dp[4]=-1 → compute
    fib(3): dp[3]=-1 → compute
      fib(2): dp[2]=-1 → compute
        fib(1) = 1
        fib(0) = 0
      dp[2] = 1  ← cached!
    dp[3] = 2  ← cached!
  dp[4] = 3  ← cached!
fib(3) → dp[3]=2  ← instant lookup, no recompute ✅
dp[5] = 5
```

Each subproblem computed **exactly once** → O(N) time, O(N) space (dp array + call stack).

---

### Approach 2 — Tabulation (Bottom-Up DP)

**Idea:** Fill dp array from small to large. No recursion — just a loop.

```
dp = [0, 1, -1, -1, -1, -1]   ← seed base cases

i=2: dp[2] = dp[1]+dp[0] = 1
i=3: dp[3] = dp[2]+dp[1] = 2
i=4: dp[4] = dp[3]+dp[2] = 3
i=5: dp[5] = dp[4]+dp[3] = 5

return dp[5] = 5 ✅
```

No call stack overhead. O(N) time, O(N) space.

---

### Approach 3 — Space Optimized

**Observation:** `dp[i]` only ever needs `dp[i-1]` and `dp[i-2]`. No need to store the full array — just two variables.

```
prev2=0, prev=1

i=2: curi = 0+1 = 1  → prev2=1, prev=1
i=3: curi = 1+1 = 2  → prev2=1, prev=2
i=4: curi = 1+2 = 3  → prev2=2, prev=3
i=5: curi = 2+3 = 5  → prev2=3, prev=5

return prev = 5 ✅
```

O(N) time, **O(1) space**.

---

### The Three Approaches — At a Glance

```
Recursion (naive):  O(2^N) time, O(N) stack   ← overlapping subproblems
Memoization:        O(N) time,   O(N) space   ← top-down, cache on the way
Tabulation:         O(N) time,   O(N) space   ← bottom-up, iterative
Space Optimized:    O(N) time,   O(1) space   ← rolling two variables
```

---

### The DP Pattern This Establishes

```
Every DP problem follows:
  1. Define the subproblem  →  dp[i] = fib number at i
  2. Base case              →  dp[0]=0, dp[1]=1
  3. Recurrence             →  dp[i] = dp[i-1] + dp[i-2]
  4. Answer                 →  dp[n]
```

Almost every 1D-DP problem you'll encounter is a variation of this exact structure.

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N) | O(N) |
| Tabulation | O(N) | O(N) |
| Space Optimized | O(N) | O(1) |
