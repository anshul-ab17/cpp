// LC 127. Word Ladder | Hard
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> words(wordList.begin(), wordList.end());
        if (!words.count(endWord)) return 0;
        queue<pair<string,int>> q; q.push({beginWord, 1});
        unordered_set<string> vis{beginWord};
        while (!q.empty()) {
            auto [word, steps] = q.front(); q.pop();
            for (int i = 0; i < word.size(); i++) {
                string nxt = word;
                for (char c = 'a'; c <= 'z'; c++) {
                    nxt[i] = c;
                    if (nxt == endWord) return steps + 1;
                    if (words.count(nxt) && !vis.count(nxt)) { vis.insert(nxt); q.push({nxt, steps+1}); }
                }
            }
        }
        return 0;
    }
};
