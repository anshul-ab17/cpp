// LC 307. Range Sum Query - Mutable | Medium (Fenwick Tree / BIT)
#include <vector>
using namespace std;

class NumArray {
    vector<int> tree, nums; int n;
    void add(int i, int d) { for (++i; i <= n; i += i&(-i)) tree[i] += d; }
    int prefix(int i) { int s = 0; for (++i; i > 0; i -= i&(-i)) s += tree[i]; return s; }
public:
    NumArray(vector<int>& nums) : n(nums.size()), nums(nums), tree(nums.size()+1, 0) {
        for (int i = 0; i < n; i++) add(i, nums[i]);
    }
    void update(int i, int val) { add(i, val - nums[i]); nums[i] = val; }
    int sumRange(int l, int r) { return prefix(r) - (l > 0 ? prefix(l-1) : 0); }
};
