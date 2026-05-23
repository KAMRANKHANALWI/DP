## Target Sum — Algorithm & Intuition

**Problem:** Given an array, assign `+` or `-` to each element. Count the number of ways to make the total expression equal to `target`.

```
arr = [1,1,1,1,1],  target = 3
→ 5 ways
  (+1+1+1+1-1), (+1+1+1-1+1), (+1+1-1+1+1), (+1-1+1+1+1), (-1+1+1+1+1)
```

---

### Intuition

**The Dream:** Try all 2^n sign assignments.

**Key Insight:** Don't simulate signs. Think in terms of two groups:

```
P = subset assigned '+'   → sum = P
N = subset assigned '-'   → sum = -N (absolute value of negatives)

P + N = total_sum   (all elements belong to one group)
P - N = target      (the expression value)

Adding both equations:
  2P = total_sum + target
   P = (total_sum + target) / 2
```

So the problem becomes: **count subsets with sum = P**. That's exactly problem 3 (Count Subsets).

---

### The Math Reduction

```
arr = [1,1,1,1,1],  target=3
total_sum = 5

P = (5 + 3) / 2 = 4

Count subsets summing to 4:
  {1,1,1,1} → 5 ways (choose which 4 elements are positive)
  → 5 ✅
```

---

### Validity Check

```
If (total_sum + target) % 2 != 0 → return 0
  (P must be an integer — impossible if sum is fractional)

If total_sum < abs(target) → return 0
  (can't achieve target even if all signs go one way)
```

---

### Why This Works

```
Every sign assignment partitions arr into:
  P elements (positive) + N elements (negative)

The expression P - N = target and P + N = total
forces P = (total + target) / 2.

Counting distinct sign assignments = counting subsets of size P.

Duplicate elements produce distinct sign assignments even
if the subset values match (just like problem 3).
```

---

### Algorithm

```
1. total = sum(arr)
2. If (total + target) % 2 != 0: return 0
3. subset_target = (total + target) // 2
4. return count_subsets(arr, subset_target)    ← problem 3
```

---

### Dry Run — `[1,1,1,1,1]`, target=3

```
total=5, subset_target=(5+3)//2=4

Count subsets of [1,1,1,1,1] summing to 4:
  Every combination of 4 elements out of 5 → C(5,4) = 5

Answer = 5 ✅
```

---

### Edge Cases

```
target > total_sum:  impossible even with all positives → 0
target < -total_sum: impossible even with all negatives → 0
(total_sum + target) is odd → P not integer → 0
```

---

### This Problem in the Family Tree

```
Subset Sum      → existence (bool)
Count Subsets   → count (int)
Target Sum      → reduce to Count Subsets via math
Partition Equal → reduce to Subset Sum via math
```

All four are the same DP. The art is in the reduction.

---

### Complexity

Same as Count Subsets with target = (total+target)//2:

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × P) | O(N × P) |
| Tabulation | O(N × P) | O(N × P) |
| Space Optimized | O(N × P) | O(P) |

Where P = (total_sum + target) / 2.