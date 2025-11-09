// LC 843. Guess the Word | Hard | Google
#include <vector>
#include <string>
using namespace std;

class Master { public: int guess(string word); };

class Solution {
    int matches(string& a, string& b) { int c = 0; for (int i = 0; i < 6; i++) c += a[i]==b[i]; return c; }
public:
    void findSecretWord(vector<string>& words, Master& master) {
        for (int t = 0; t < 10; t++) {
            string g = words[rand() % words.size()];
            int res = master.guess(g);
            if (res == 6) return;
            vector<string> nxt;
            for (auto& w : words) if (matches(w, g) == res) nxt.push_back(w);
            words = nxt;
        }
    }
};
