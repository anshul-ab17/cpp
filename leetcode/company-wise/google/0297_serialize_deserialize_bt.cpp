// LC 297. Serialize and Deserialize Binary Tree | Hard | Google
#include <string>
#include <sstream>
#include <queue>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int x) : val(x), left(nullptr), right(nullptr) {} };

class Codec {
public:
    string serialize(TreeNode* root) {
        if (!root) return "N";
        return to_string(root->val) + "," + serialize(root->left) + "," + serialize(root->right);
    }
    TreeNode* deserialize(string data) {
        istringstream ss(data); return build(ss);
    }
private:
    TreeNode* build(istringstream& ss) {
        string val; getline(ss, val, ',');
        if (val == "N") return nullptr;
        TreeNode* node = new TreeNode(stoi(val));
        node->left = build(ss); node->right = build(ss);
        return node;
    }
};
