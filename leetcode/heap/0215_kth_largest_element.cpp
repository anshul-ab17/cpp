// LC 215. Kth Largest Element in an Array | Medium
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int n : nums) { pq.push(n); if (pq.size() > k) pq.pop(); }
        return pq.top();
    }
};
