// LC 70. Climbing Stairs | Easy
class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 1;
        for (int i = 1; i < n; i++) { int t = b; b += a; a = t; }
        return b;
    }
};
