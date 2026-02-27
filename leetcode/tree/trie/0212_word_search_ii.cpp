// LC 212. Word Search II | Hard
#include <vector>
#include <string>
using namespace std;

class Solution {
    struct Trie { Trie* ch[26] = {}; string word; };
    int m, n;
    void dfs(vector<vector<char>>& b, int i, int j, Trie* node, vector<string>& res) {
        char c = b[i][j];
        if (c == '#' || !node->ch[c-'a']) return;
        node = node->ch[c-'a'];
        if (!node->word.empty()) { res.push_back(node->word); node->word.clear(); }
        b[i][j] = '#';
        int d[] = {0,1,0,-1,0};
        for (int x = 0; x < 4; x++) {
            int ni = i+d[x], nj = j+d[x+1];
            if (ni >= 0 && ni < m && nj >= 0 && nj < n) dfs(b, ni, nj, node, res);
        }
        b[i][j] = c;
    }
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie* root = new Trie();
        for (auto& w : words) {
            Trie* n = root;
            for (char c : w) { if (!n->ch[c-'a']) n->ch[c-'a'] = new Trie(); n = n->ch[c-'a']; }
            n->word = w;
        }
        m = board.size(); n = board[0].size(); vector<string> res;
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) dfs(board, i, j, root, res);
        return res;
    }
};
