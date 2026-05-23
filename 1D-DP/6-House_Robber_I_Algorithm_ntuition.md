## House Robber I — Algorithm & Intuition

**Problem:** You are a robber on a street of `n` houses. Each house has money `nums[i]`. You can't rob two adjacent houses (alarm triggers). Maximise the total money robbed.

```
nums = [2, 7, 9, 3, 1]
→ rob houses 0, 2, 4: 2+9+1 = 12  ✅
```

---

### Intuition

**The Dream:** Rob every house.

**Key Insight:** House Robber I is **identical** to Max Sum of Non-Adjacent Elements — just with a story attached. The constraint "can't rob adjacent houses" maps exactly to "can't pick adjacent elements".

```
nums = [2, 7, 9, 3, 1]
         ↑     ↑   ↑
      pick 2, skip 7, pick 9, skip 3, pick 1 → 12

OR   skip 2, pick 7, skip 9, pick 3, skip 1 → 10

Max = 12  ✅
```

---

### The Two Choices at Each House

```
At house i, you decide:

ROB it:       nums[i] + best_from(i-2)   ← skip i-1, use dp[i-2]
SKIP it:      best_from(i-1)             ← dp[i-1]

dp[i] = max(rob, skip)
```

---

### Dry Run — `[2, 7, 9, 3, 1]`

```
dp[0] = 2   ← only one house, rob it

i=1:
  rob  = nums[1] + dp[-1] = 7+0 = 7
  skip = dp[0] = 2
  dp[1] = 7

i=2:
  rob  = nums[2] + dp[0] = 9+2 = 11
  skip = dp[1] = 7
  dp[2] = 11

i=3:
  rob  = nums[3] + dp[1] = 3+7 = 10
  skip = dp[2] = 11
  dp[3] = 11

i=4:
  rob  = nums[4] + dp[2] = 1+11 = 12
  skip = dp[3] = 11
  dp[4] = 12

Answer = 12 ✅   (rob houses at index 0, 2, 4 → 2+9+1)
```

---

### Space Optimized Trace

```
prev2=0, prev=2

i=1: pick=7+0=7,  not=2   → curi=7,  prev2=2,  prev=7
i=2: pick=9+2=11, not=7   → curi=11, prev2=7,  prev=11
i=3: pick=3+7=10, not=11  → curi=11, prev2=11, prev=11
i=4: pick=1+11=12,not=11  → curi=12, prev2=11, prev=12

return 12 ✅
```

---

### House Robber vs Non-Adjacent Sum

```
Non-Adjacent Sum:   generic array problem
House Robber I:     same problem, "houses" framing
House Robber II:    circular houses — slight variation (next problem)

The code is literally the same — only the variable names differ.
```

---

### Recurrence Summary

```
dp[0] = nums[0]

dp[i] = max(
    nums[i] + (dp[i-2] if i >= 2 else 0),
    dp[i-1]
)

Answer = dp[n-1]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Recursive | O(2^N) | O(N) |
| Memoization | O(N) | O(N) |
| Tabulation | O(N) | O(N) |
| Space Optimized | O(N) | O(1) |
