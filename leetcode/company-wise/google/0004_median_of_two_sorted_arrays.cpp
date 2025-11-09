// LC 4. Median of Two Sorted Arrays | Hard | Google
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) swap(nums1, nums2);
        int m = nums1.size(), n = nums2.size(), lo = 0, hi = m;
        while (lo <= hi) {
            int i = (lo+hi)/2, j = (m+n+1)/2 - i;
            int la = i > 0 ? nums1[i-1] : INT_MIN, ra = i < m ? nums1[i] : INT_MAX;
            int lb = j > 0 ? nums2[j-1] : INT_MIN, rb = j < n ? nums2[j] : INT_MAX;
            if (la <= rb && lb <= ra)
                return (m+n)%2 ? max(la,lb) : (max(la,lb)+min(ra,rb))/2.0;
            else if (la > rb) hi = i-1;
            else lo = i+1;
        }
        return 0;
    }
};
