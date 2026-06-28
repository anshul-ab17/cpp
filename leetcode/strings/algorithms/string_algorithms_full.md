# String Algorithms

## Algorithms You Must Know

1. KMP (Knuth Morris Pratt) ⭐⭐⭐
2. Rabin Karp ⭐⭐⭐
3. Z Algorithm ⭐⭐⭐
4. Rolling Hash ⭐⭐⭐⭐
5. Manacher's Algorithm ⭐⭐⭐⭐⭐
6. Trie + String Matching ⭐⭐⭐
7. Aho-Corasick ⭐⭐⭐⭐⭐
8. Suffix Array ⭐⭐⭐⭐⭐
9. LCP Array ⭐⭐⭐⭐

---

# 1. KMP Algorithm

Used for:
- Pattern matching in O(N + M)

Problems:
- LC 28 - Find the Index of the First Occurrence
- LC 459 - Repeated Substring Pattern
- LC 1392 - Longest Happy Prefix

## LPS Construction
## KMP Search
---

# 2. Rabin Karp

Average O(N)

Uses rolling hash.
---

# 3. Z Algorithm

Z[i] = longest prefix starting at i.
---

# 4. Rolling Hash
Problems:
- LC 1044 Longest Duplicate Substring
- LC 214 Shortest Palindrome

---

# 5. Manacher Algorithm

Find all palindromes in O(N).
Problem:
- LC 5 Longest Palindromic Substring

---

# 6. Trie + Strings

Problems:
- LC 208
- LC 211
- LC 212

---

# 7. Aho-Corasick

Multi-pattern matching.

Complexity:
O(text + patterns + matches)

Used in:
- search engines
- IDS systems

---

# 8. Suffix Array

Sort all suffixes.

Applications:
- substring queries
- lexicographic queries

Complexity:
O(N log N)

---

# 9. LCP Array

Longest Common Prefix between adjacent suffixes.

Kasai Algorithm:
O(N)

---

# Recognition Guide

If problem says:

- pattern search -> KMP / Rabin Karp
- many patterns -> Trie / Aho-Corasick
- longest palindrome -> Manacher
- duplicate substring -> Rolling Hash
- prefix suffix -> KMP / Z
- suffix ordering -> Suffix Array

---

# Important Problems

- LC 28
- LC 214
- LC 459
- LC 1044
- LC 1392
- LC 1923
- LC 2223
