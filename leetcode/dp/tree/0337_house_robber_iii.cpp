// LC 337. House Robber III | Medium (DP on Tree)
#include <algorithm>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} };

class Solution {
    pair<int,int> dfs(TreeNode* n) {
        if (!n) return {0, 0};
        auto [lr, ls] = dfs(n->left);
        auto [rr, rs] = dfs(n->right);
        return {n->val + ls + rs, max(lr, ls) + max(rr, rs)};
    }
public:
    int rob(TreeNode* root) { auto [r, s] = dfs(root); return max(r, s); }
};
