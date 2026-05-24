## Print Longest Increasing Subsequence — Algorithm & Intuition

**Problem:** Don't just find the LIS length — **reconstruct and print the actual sequence**.

```
arr = [5, 4, 11, 1, 16, 8]
→ LIS = [5, 11, 16]  or  [4, 11, 16]  or  [1, 8, 16] — depends on tie-breaking
```

---

### Intuition

**The Dream:** Know not just how long the LIS is, but which elements form it.

**Key Insight:** During the O(N²) DP, track for each index `i`: **which previous index** contributed to the best extension at `i`. This is the `hash_arr` — a "parent pointer" array. After computing dp, follow these parent pointers backwards from the endpoint of the overall longest LIS.

---

### Two Arrays

```
dp[i]       = length of LIS ending at index i
hash_arr[i] = the previous index in the best LIS ending at i
              (points to itself if i is the start of its LIS)
```

---

### Building the Arrays

```
For each i:
    For each prev < i:
        If arr[prev] < arr[i] AND 1 + dp[prev] > dp[i]:
            dp[i] = 1 + dp[prev]
            hash_arr[i] = prev      ← remember where we came from
```

The `hash_arr[i] = prev` is set only when we actually update `dp[i]`. Initially `hash_arr[i] = i` (self-pointer = "I am the start of my LIS").

---

### Dry Run — `[5, 4, 11, 1, 16, 8]`

```
Initial: dp=[1,1,1,1,1,1], hash=[0,1,2,3,4,5]

i=0 (5):  no prev → dp[0]=1, hash[0]=0
i=1 (4):  5>4 → skip → dp[1]=1, hash[1]=1
i=2 (11): 5<11✅ → dp=2, hash[2]=0
           4<11✅ → 1+1=2, not better → no update
           dp[2]=2, hash[2]=0
i=3 (1):  all prev > 1 → dp[3]=1, hash[3]=3
i=4 (16): 5<16✅  → dp=2, hash[4]=0
           4<16✅  → 1+1=2, not better
           11<16✅ → 1+2=3 > 2, UPDATE dp[4]=3, hash[4]=2
           1<16✅  → 1+1=2, not better
           dp[4]=3, hash[4]=2
i=5 (8):  5<8✅  → dp=2, hash[5]=0
           4<8✅  → 1+1=2, not better
           11>8   → skip
           1<8✅  → 1+1=2, not better
           dp[5]=2, hash[5]=0

dp       = [1, 1, 2, 1, 3, 2]
hash_arr = [0, 1, 0, 3, 2, 0]

maxi=3 at last_index=4
```

---

### Reconstruction

```
Start at last_index=4 (arr[4]=16)

LIS = [16]

While hash_arr[last_index] != last_index:
    last_index = hash_arr[last_index]
    LIS.append(arr[last_index])

Step 1: hash_arr[4]=2 ≠ 4 → last_index=2, LIS=[16, 11]
Step 2: hash_arr[2]=0 ≠ 2 → last_index=0, LIS=[16, 11, 5]
Step 3: hash_arr[0]=0 == 0 → STOP

LIS.reverse() → [5, 11, 16] ✅
```

---

### The Self-Pointer Termination Trick

```
hash_arr[i] = i means "I am the start of my own LIS chain".
The while loop stops when it reaches the start of the chain.

This is cleaner than storing -1 or None:
  hash_arr[last_index] != last_index → keep walking back
  hash_arr[last_index] == last_index → reached chain start → stop
```

---

### Multiple LIS of the Same Length

```
When 1 + dp[prev] == dp[i] (equal, not strictly greater):
    The condition is `1 + dp[prev] > dp[i]` → not updated.
    So hash_arr[i] records only the FIRST parent that achieved the max.

Different tie-breaking gives different valid LIS sequences.
All are correct.
```

---

### Complexity

| Phase | Time | Space |
|---|---|---|
| Build dp + hash_arr | O(N²) | O(N) |
| Reconstruct | O(N) | O(N) |
| Total | O(N²) | O(N) |
