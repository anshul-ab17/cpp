// LC 202. Happy Number | Easy
class Solution {
    int nxt(int n) { int s = 0; while (n) { int d = n % 10; s += d*d; n /= 10; } return s; }
public:
    bool isHappy(int n) {
        int slow = n, fast = nxt(n);
        while (fast != 1 && slow != fast) { slow = nxt(slow); fast = nxt(nxt(fast)); }
        return fast == 1;
    }
};
