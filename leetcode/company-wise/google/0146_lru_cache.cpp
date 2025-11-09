// LC 146. LRU Cache | Medium | Google, Amazon, Microsoft
#include <unordered_map>
#include <list>
using namespace std;

class LRUCache {
    int cap;
    list<pair<int,int>> dll;
    unordered_map<int, list<pair<int,int>>::iterator> mp;
public:
    LRUCache(int capacity) : cap(capacity) {}
    int get(int key) {
        if (!mp.count(key)) return -1;
        dll.splice(dll.end(), dll, mp[key]);
        return mp[key]->second;
    }
    void put(int key, int value) {
        if (mp.count(key)) { mp[key]->second = value; dll.splice(dll.end(), dll, mp[key]); return; }
        if (dll.size() == cap) { mp.erase(dll.front().first); dll.pop_front(); }
        dll.push_back({key, value}); mp[key] = prev(dll.end());
    }
};
