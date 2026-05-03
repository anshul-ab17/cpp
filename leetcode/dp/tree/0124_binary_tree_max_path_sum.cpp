// LC 124. Binary Tree Maximum Path Sum | Hard (DP on Tree)
#include <algorithm>
#include <climits>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} };

class Solution {
    int ans = INT_MIN;
    int dfs(TreeNode* n) {
        if (!n) return 0;
        int l = max(dfs(n->left), 0), r = max(dfs(n->right), 0);
        ans = max(ans, n->val + l + r);
        return n->val + max(l, r);
    }
public:
    int maxPathSum(TreeNode* root) { dfs(root); return ans; }
};
