// LC 380. Insert Delete GetRandom O(1) | Medium | Microsoft
#include <vector>
#include <unordered_map>
using namespace std;

class RandomizedSet {
    vector<int> v; unordered_map<int,int> mp;
public:
    bool insert(int val) { if (mp.count(val)) return false; mp[val]=v.size(); v.push_back(val); return true; }
    bool remove(int val) {
        if (!mp.count(val)) return false;
        int i = mp[val], last = v.back();
        v[i] = last; mp[last] = i; v.pop_back(); mp.erase(val); return true;
    }
    int getRandom() { return v[rand()%v.size()]; }
};
