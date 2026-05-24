## Minimum Insertions and Deletions to Convert s1 to s2 — Algorithm & Intuition

**Problem:** Given two strings `s1` and `s2`, find the minimum number of **insertions and deletions** required to convert `s1` into `s2`.

```
s1 = "heap",  s2 = "pea"
→ 3 operations  (delete 'h', delete 'a', insert 'p' at start... wait)

LCS("heap","pea") = "ea" (length 2)
deletions  = 4 - 2 = 2   (delete 'h','p' from s1... hmm)

Actually:
  LCS = "ea" (length 2)
  deletions  = len(s1) - LCS = 4-2 = 2   (chars in s1 not in LCS)
  insertions = len(s2) - LCS = 3-2 = 1   (chars in s2 not in LCS)
  total = 3 ✅
```

---

### Intuition

**The Dream:** Convert s1 to s2 with as few operations as possible.

**Key Insight:** The LCS is the "free zone" — characters in the LCS don't need to move. Every other character in s1 must be deleted, and every other character needed in s2 must be inserted.

```
LCS = characters shared in the same order → keep these, they're free
Non-LCS chars in s1 → must DELETE  (count = n - LCS)
Non-LCS chars in s2 → must INSERT  (count = m - LCS)

Total = (n - LCS) + (m - LCS) = n + m - 2 × LCS
```

---

### The Math

```
s1 = "heap"  (n=4)
s2 = "pea"   (m=3)

LCS("heap","pea"):
     ""  p  e  a
""  [ 0,  0,  0,  0 ]
h   [ 0,  0,  0,  0 ]
e   [ 0,  0,  1,  1 ]
a   [ 0,  0,  1,  2 ]
p   [ 0,  1,  1,  2 ]

LCS = 2  ("ea")

deletions  = 4 - 2 = 2   (delete 'h' and 'p' from s1)
insertions = 3 - 2 = 1   (insert 'p' into s1)
total = 3 ✅

"heap" → delete h,p → "ea" → insert p at start → "pea" ✅
```

---

### Why This is Optimal

```
Any conversion from s1 to s2 must:
  Remove characters in s1 that aren't in the final shared core.
  Add characters from s2 that don't already exist in s1.

The largest possible "shared core" = LCS → maximises what you keep free.
Minimising operations = maximising what you keep = maximising LCS.
```

---

### Relationship to Other Problems

```
Min Insertions to Palindrome:
  s2 = reverse(s1), same length → deletions = 0 (not used)
  Only insertions: n - LPS = n - LCS(s, rev)
  Special case of this problem where s2 = rev(s1)

General (this problem):
  s1 → s2 arbitrary
  Both insertions and deletions: (n-LCS) + (m-LCS) = n+m-2×LCS

Edit Distance (different problem):
  Also allows substitutions → different DP
```

---

### Algorithm — One Line After LCS

```
lcs = dp[n][m]       ← standard LCS computation
deletions  = n - lcs
insertions = m - lcs
return insertions + deletions
```

---

### Recurrence Summary

```
LCS dp table (standard):
  dp[i][j] = 1 + dp[i-1][j-1]          if s1[i-1] == s2[j-1]
           = max(dp[i-1][j], dp[i][j-1]) otherwise

lcs = dp[n][m]
Answer = (n - lcs) + (m - lcs) = n + m - 2 × lcs
```

---

### Complexity

| | Time | Space |
|---|---|---|
| Build LCS | O(N × M) | O(N × M) |
| Compute answer | O(1) | O(1) |
| Total | O(N × M) | O(N × M) |
