## Longest Increasing Subsequence — Algorithm & Intuition

**Problem:** Find the length of the longest subsequence of an array where every element is strictly greater than the previous one.

```
arr = [10, 9, 2, 5, 3, 7, 101, 18]
→ LIS = [2, 3, 7, 18] or [2, 5, 7, 101],  length = 4
```

---

### Intuition

**The Dream:** Pick as many elements as possible in strictly increasing order.

**Key Insight:** At each index `i`, you either include it in the LIS (if it's greater than the previously chosen element) or skip it.

---

### Approach 1 — Recursion with (idx, prev_idx)

```
State: (idx, prev_idx)
  idx      = current element being considered
  prev_idx = index of last element INCLUDED in LIS (-1 if none yet)

lis(idx, prev_idx):
    if idx == n: return 0

    not_pick = lis(idx+1, prev_idx)

    pick = 0
    if prev_idx == -1 or arr[idx] > arr[prev_idx]:
        pick = 1 + lis(idx+1, idx)   ← idx becomes new prev

    return max(pick, not_pick)
```

`+1` in the dp indexing for `prev_idx` because it can be -1 (shift by 1 to use as array index).

---

### Approach 2 — Classic O(N²) DP (Most Commonly Asked)

```
dp[i] = length of LIS ENDING at index i

Every element alone is an LIS of length 1 → dp = [1]*n

For each i, look at all prev < i:
    If arr[prev] < arr[i]:   ← increasing condition
        dp[i] = max(dp[i], 1 + dp[prev])

Answer = max(dp)
```

---

### Dry Run — `[10, 9, 2, 5, 3, 7, 101, 18]`

```
Initial dp: [1, 1, 1, 1, 1, 1, 1, 1]

i=0 (10): no prev → dp[0]=1
i=1 (9):  10>9 → no update → dp[1]=1
i=2 (2):  10>2, 9>2 → no update → dp[2]=1
i=3 (5):  10>5, 9>5, 2<5 ✅ → dp[3]=max(1,1+dp[2])=2  → dp[3]=2
i=4 (3):  10>3, 9>3, 2<3 ✅ → dp[4]=max(1,1+1)=2 → dp[4]=2
i=5 (7):  10>7, 9>7, 2<7✅→dp=2, 5<7✅→dp=max(2,1+2)=3, 3<7✅→max(3,1+2)=3 → dp[5]=3
i=6 (101):all < 101 → dp[6] = 1+max(dp[0..5]) = 1+3 = 4
i=7 (18): 10<18✅→2, 9<18✅→2, 2<18✅→2, 5<18✅→3, 3<18✅→3, 7<18✅→4 → dp[7]=4

dp = [1, 1, 1, 2, 2, 3, 4, 4]
max = 4 ✅
```

---

### Why dp[i] = "ending at i", Not "starting at i"

```
"Ending at i" is preferred for tabulation:
  When computing dp[i], all dp[0..i-1] are already computed.
  Look backwards → no dependency issues.

"Starting at i" would require knowing future elements:
  dp[i] = LIS starting at i → need dp[i+1..n] → fill backwards.
  The memoization version in the code uses this direction.
  Both are valid; "ending" version is simpler for tabulation.
```

---

### Approach Comparison

```
Approach                | Time       | Space   | Reconstruct?
------------------------|------------|---------|-------------
Recursion (no memo)     | O(2^N × N) | O(N)    | No
Memoization (idx,prev)  | O(N²)      | O(N²)   | Hard
Tabulation O(N²) dp[i] | O(N²)      | O(N)    | Yes (problem 2)
Binary Search           | O(N log N) | O(N)    | No (next problem)
```

---

### Recurrence Summary

```
dp[i] = 1   for all i   (base case)

For i from 0 to n-1:
    For prev from 0 to i-1:
        If arr[prev] < arr[i]:
            dp[i] = max(dp[i], 1 + dp[prev])

Answer = max(dp)
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization (idx,prev) | O(N²) | O(N²) |
| Tabulation dp[i] | O(N²) | O(N) |
| Space Optimized | O(N²) | O(N) |
