## Shortest Common Supersequence — Algorithm & Intuition

**Problem:** Find the **shortest string that contains both s1 and s2 as subsequences**.

```
s1 = "brute",  s2 = "groot"
→ SCS = "bgruoote"  (length 8)
```

---

### Intuition

**The Dream:** Merge two strings as tightly as possible — share as many characters as you can.

**Key Insight:** Every character in the LCS appears in both strings. In the SCS, we only need to include LCS characters **once** (shared). All other characters appear separately.

```
SCS length = n + m - LCS

Proof:
  Total characters = n (from s1) + m (from s2)
  LCS characters are counted twice but included once
  → subtract LCS once: n + m - LCS
```

---

### Length is Easy — Reconstruction is the Challenge

```
SCS length = n + m - LCS(s1, s2)

For "brute" (n=5) and "groot" (m=5):
  LCS = "rot" (length 3)... let me verify.

LCS("brute","groot"):
     ""  g  r  o  o  t
""  [ 0,  0,  0,  0,  0,  0 ]
b   [ 0,  0,  0,  0,  0,  0 ]
r   [ 0,  0,  1,  1,  1,  1 ]
u   [ 0,  0,  1,  1,  1,  1 ]
t   [ 0,  0,  1,  1,  1,  2 ]
e   [ 0,  0,  1,  1,  1,  2 ]

LCS = 2 ("rt")
SCS length = 5+5-2 = 8 ✅
```

---

### Reconstruction — Backtrack Through DP Table

The SCS contains all characters of both strings. During backtracking:

```
At (i, j):

Match (s1[i-1] == s2[j-1]):
    → ADD this character ONCE (it's shared)
    → Move diagonally: i--, j--

No match:
    → ADD whichever character we "came from" to get here
    → If dp[i-1][j] > dp[i][j-1]:
          ADD s1[i-1] (moved from above)
          i--
      Else:
          ADD s2[j-1] (moved from left)
          j--

After loop exhausts one string:
    Add all remaining characters from the other string.

Reverse at the end.
```

---

### Dry Run — `s1="brute"`, `s2="groot"`

```
DP table:
     ""  g  r  o  o  t
""  [ 0,  0,  0,  0,  0,  0 ]
b   [ 0,  0,  0,  0,  0,  0 ]
r   [ 0,  0,  1,  1,  1,  1 ]
u   [ 0,  0,  1,  1,  1,  1 ]
t   [ 0,  0,  1,  1,  1,  2 ]
e   [ 0,  0,  1,  1,  1,  2 ]

Backtrack from (5,5):
  (5,5): 'e'≠'t' → dp[4][5]=2, dp[5][4]=1 → 2>1 → add s1[4]='e', i=4
  (4,5): 't'='t' → MATCH → add 't', i=3, j=4
  (3,4): 'u'≠'o' → dp[2][4]=1, dp[3][3]=1 → equal → add s2[3]='o', j=3
  (3,3): 'u'≠'o' → dp[2][3]=1, dp[3][2]=1 → equal → add s2[2]='o', j=2
  (3,2): 'u'≠'r' → dp[2][2]=1, dp[3][1]=0 → 1>0 → add s1[2]='u', i=2
  (2,2): 'r'='r' → MATCH → add 'r', i=1, j=1
  (1,1): 'b'≠'g' → dp[0][1]=0, dp[1][0]=0 → equal → add s2[0]='g', j=0
  j=0 → add remaining s1: s1[0]='b'

Collected: e,t,o,o,u,r,g,b → reverse → "bgruoote" ✅
```

---

### Match vs No-Match in SCS Backtracking

```
LCS backtracking:  collect only MATCHED characters (skip unmatched)
SCS backtracking:  collect EVERY character:
                    matched  → add once (shared)
                    unmatched → add from whichever string it came from

SCS includes everything; LCS filters to common characters only.
```

---

### Remaining Characters After Loop

```
When i=0 but j>0:
  All remaining s2[0..j-1] haven't been added yet → add them.

When j=0 but i>0:
  All remaining s1[0..i-1] → add them.

These are characters from the string that "ran out" first during backtracking.
```

---

### Recurrence Summary

```
LCS table (standard):
  dp[i][j] = 1 + dp[i-1][j-1]         if match
           = max(dp[i-1][j], dp[i][j-1]) if no match

SCS length = n + m - dp[n][m]

Reconstruction: backtrack adding every character,
  matched chars once, unmatched from their respective string.
  Reverse at end.
```

---

### Complexity

| Phase | Time | Space |
|---|---|---|
| Build LCS table | O(N × M) | O(N × M) |
| Backtrack | O(N + M) | O(N + M) |
| Total | O(N × M) | O(N × M) |
