class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int currentMax = 0;
        int tempMax = 0;
        for(int num : nums) {
            if(num == 1) {
                tempMax++;
                currentMax = max(tempMax, currentMax);
            }
            else {
                tempMax = 0;
            }
        }
        return currentMax;
    }
};