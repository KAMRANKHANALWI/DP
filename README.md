# Dynamic Programming

A structured collection of dynamic programming problems — grouped by pattern, each with a clean Python solution and the Algorithm & Intuition breakdown covering the key insight, dry runs, and complexity.

Every problem is implemented across all applicable approaches: Recursion → Memoization → Tabulation → Space Optimized.

---

## 1D DP

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Fibonacci | Gateway DP — all four approaches explained |
| 2 | Climbing Stairs | Fib with different base case; generalises to k-steps |
| 3 | Frog Jump | min + cost instead of sum; same 2-state dependency |
| 4 | Frog Jump K Distance | Inner loop over k choices replaces hardcoded 2 |
| 5 | Max Sum Non-Adjacent Elements | Pick/not-pick pattern; why dp[i-2] when you pick |
| 6 | House Robber I | Same as above, linear arrangement |
| 7 | House Robber II | Two-slice trick to handle circular constraint |

## 2D Grid DP

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Ninja's Training | 2D state (day × last activity); last=3 sentinel |
| 2 | Grid Unique Paths | paths(i,j) = paths(i-1,j) + paths(i,j-1) |
| 3 | Grid Path with Obstacle | Reset to 0 on blocked cell; zero propagates forward |
| 4 | Minimum Path Sum Grid | OOB = ∞ (vs 0 for counting) — same structure, different goal |
| 5 | Triangle | Bottom-up cleaner; dp[i][j] = val + min(down, diagonal) |
| 6 | Maximum Falling Path Sum | Variable start + end; 3-direction movement |

## Knapsack / Subsequences DP

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Subset Sum | Pick/not-pick; OR combination → bool |
| 2 | Partition Equal Subset Sum | Reduces to Subset Sum with target = total//2 |
| 3 | Count Subsets with Sum K | Same as Subset Sum but + instead of OR |
| 4 | 0/1 Knapsack | Pick reads dp[idx-1] (each item once) |
| 5 | Minimum Coins | Pick reads dp[idx] (unbounded reuse) |
| 6 | Target Sum | Math reduction: P = (total+target)//2 → Count Subsets |
| 7 | Coin Change II | Unbounded + count; combinations not permutations |

## LCS Family / String DP

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Longest Common Subsequence | Match → diagonal+1; mismatch → max(up, left) |
| 2 | Print LCS | Backtrack through DP table; reverse at end |
| 3 | Longest Common Substring | Reset dp[i][j]=0 on mismatch; track global max |
| 4 | Longest Palindromic Subsequence | LCS(s, reverse(s)) |
| 5 | Minimum Insertions to Palindrome | n - LPS |
| 6 | Min Insertions and Deletions | (n - LCS) + (m - LCS) |
| 7 | Shortest Common Supersequence | n+m−LCS length; backtrack adding every character |

## LIS

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Longest Increasing Subsequence | dp[i] = LIS ending at i; O(N²) tabulation |
| 2 | Print LIS | Parent pointer array (hash_arr); self-pointer termination |
| 3 | LIS — Binary Search | temp[] stores optimal tails; temp ≠ actual LIS |

## Stocks DP

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Buy and Sell I | Greedy: track running min; O(N) one pass |
| 2 | Buy and Sell II | 2-state DP (idx, buy); generalises to constrained variants |

---

## Structure

Each problem has two files:

```
N-problem_name.py                        # solution (all approaches)
N-Problem_Name — Algorithm & Intuition.md   # breakdown
```

---

## Topics Covered

`pick/not-pick` · `unbounded knapsack` · `interval DP` · `string DP` · `LCS family` · `LIS` · `grid traversal` · `state machine` · `binary search optimization` · `space optimization`