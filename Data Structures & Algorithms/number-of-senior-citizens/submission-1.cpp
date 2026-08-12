class Solution {
public:
    int countSeniors(vector<string>& details) {
        int count = 0;

        for(int i = 0; i < details.size(); i++) {
            string detail = details[i].substr(11, 2);
            int detail_num = std::stoi(detail);
            if(detail_num > 60) {
                count++;
            }
        }
        return count;
    }
};