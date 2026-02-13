// LC 191. Number of 1 Bits | Easy
class Solution {
public:
    int hammingWeight(int n) { int c = 0; while (n) { n &= n-1; c++; } return c; }
    int hammingWeight_builtin(int n) { return __builtin_popcount(n); }
};
