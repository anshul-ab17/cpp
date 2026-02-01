// LC 98. Validate Binary Search Tree | Medium
#include <climits>
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} };

class Solution {
    bool check(TreeNode* n, long lo, long hi) {
        if (!n) return true;
        if (n->val <= lo || n->val >= hi) return false;
        return check(n->left, lo, n->val) && check(n->right, n->val, hi);
    }
public:
    bool isValidBST(TreeNode* root) { return check(root, LONG_MIN, LONG_MAX); }
};
