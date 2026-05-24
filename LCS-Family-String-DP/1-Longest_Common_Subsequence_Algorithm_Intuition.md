## Longest Common Subsequence — Algorithm & Intuition

**Problem:** Given two strings `s1` and `s2`, find the length of their **longest common subsequence** (LCS) — the longest sequence of characters that appears in both strings in the same relative order, but not necessarily contiguously.

```
s1 = "abcde",  s2 = "ace"
→ LCS = "ace",  length = 3
```

---

### Intuition

**The Dream:** Find as long a shared sequence as possible.

**Key Insight:** Compare the last characters of the current substrings. Two cases:

```
Case 1: s1[i] == s2[j]
    Both characters are part of LCS → take this match and move inward diagonally
    lcs(i,j) = 1 + lcs(i-1, j-1)

Case 2: s1[i] != s2[j]
    Skip one of them — try both, take the better:
    lcs(i,j) = max(lcs(i-1, j), lcs(i, j-1))
```

---

### The DP State

```
dp[i][j] = length of LCS of s1[0..i-1] and s2[0..j-1]
           (1-indexed in tabulation — row 0 and col 0 represent empty strings)

LCS with empty string = 0 → dp[i][0] = dp[0][j] = 0 for all i,j
```

---

### Dry Run — `s1="abcde"`, `s2="ace"`

```
     ""  a  c  e
""  [ 0,  0,  0,  0 ]
a   [ 0,  1,  1,  1 ]
b   [ 0,  1,  1,  1 ]
c   [ 0,  1,  2,  2 ]
d   [ 0,  1,  2,  2 ]
e   [ 0,  1,  2,  3 ]

dp[1][1]: s1[0]='a'==s2[0]='a' → 1+dp[0][0]=1
dp[2][1]: s1[1]='b'!=s2[0]='a' → max(dp[1][1]=1, dp[2][0]=0) = 1
dp[3][2]: s1[2]='c'==s2[1]='c' → 1+dp[2][1]=2
dp[5][3]: s1[4]='e'==s2[2]='e' → 1+dp[4][2]=3

Answer = dp[5][3] = 3 ✅
```

---

### Shifted Indexing in Tabulation

```
Recursion uses 0-indexed strings with i,j going to -1 (base case).
Tabulation shifts by 1: dp[i][j] = LCS of first i chars of s1, first j of s2.

s1[i-1] maps to the i-th character (1-indexed).

This avoids negative indices and cleanly handles the empty string base.
```

---

### The Three Moves in the DP Table

```
Match    → dp[i][j] = 1 + dp[i-1][j-1]   (diagonal up-left)
Skip s1  → dp[i][j] = dp[i-1][j]         (up)
Skip s2  → dp[i][j] = dp[i][j-1]         (left)
```

```
Visual direction of decisions in the table:

    s2 →
s1  [0, 0, 0, 0]
↓   [0, ↖  ←  ←]   ↖ = match (diagonal)
    [0, ↑  ↖  ←]   ↑ = skip s1 (up)
    [0, ↑  ↑  ↖]   ← = skip s2 (left)
```

---

### Space Optimization — One Row

```
Only the previous row is needed:
  dp[i][j] uses dp[i-1][j-1] and dp[i-1][j]
  → prev row + current row suffice

prev[j] = dp[i-1][j]
curr[j] = dp[i][j]

For the diagonal (dp[i-1][j-1]):
  Use prev[j-1] — already computed in previous iteration of outer loop.
```

---

### LCS as a Gateway

LCS is the core of the entire LCS-Family section. The next 6 problems all reduce to or build on this:

```
Print LCS         → backtrack through LCS table
Longest Substring → same table, reset on mismatch
Palindromic Subseq → LCS(s, reverse(s))
Min Insertions    → n - LPS
Min Insert/Delete → n+m - 2×LCS
Shortest Superseq → n+m - LCS (length), backtrack to reconstruct
```

---

### Recurrence Summary

```
dp[0][j] = 0, dp[i][0] = 0   for all i,j

If s1[i-1] == s2[j-1]:  dp[i][j] = 1 + dp[i-1][j-1]
Else:                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Answer = dp[n][m]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × M) | O(N × M) |
| Tabulation | O(N × M) | O(N × M) |
| Space Optimized | O(N × M) | O(M) |
