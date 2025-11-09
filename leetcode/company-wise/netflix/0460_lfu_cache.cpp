// LC 460. LFU Cache | Hard | Netflix
#include <unordered_map>
#include <list>
using namespace std;

class LFUCache {
    int cap, minFreq;
    unordered_map<int, pair<int,int>> kv; // key -> {val, freq}
    unordered_map<int, list<int>> freq_list;
    unordered_map<int, list<int>::iterator> pos;

    void update(int key) {
        int f = kv[key].second;
        freq_list[f].erase(pos[key]);
        if (freq_list[f].empty() && f == minFreq) minFreq++;
        kv[key].second++;
        freq_list[f+1].push_back(key);
        pos[key] = prev(freq_list[f+1].end());
    }
public:
    LFUCache(int capacity) : cap(capacity), minFreq(0) {}
    int get(int key) { if (!kv.count(key)) return -1; update(key); return kv[key].first; }
    void put(int key, int value) {
        if (cap <= 0) return;
        if (kv.count(key)) { kv[key].first = value; update(key); return; }
        if ((int)kv.size() >= cap) {
            int evict = freq_list[minFreq].front();
            freq_list[minFreq].pop_front(); pos.erase(evict); kv.erase(evict);
        }
        kv[key] = {value, 1}; freq_list[1].push_back(key);
        pos[key] = prev(freq_list[1].end()); minFreq = 1;
    }
};
