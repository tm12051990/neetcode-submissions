#include <unordered_map>

class Solution {
public:
    int largestUniqueNumber(vector<int>& nums) {
        unordered_map<int, int> seen;

        for(int num : nums) {
            seen[num]++;
        }
        int largest = -1;

        for(auto& entry : seen) {
            if(entry.second == 1) {
                largest = max(largest, entry.first);
            }
        }
        return largest;
    }
};
