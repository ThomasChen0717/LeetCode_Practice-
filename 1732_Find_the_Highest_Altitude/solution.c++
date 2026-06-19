// Approach: Prefix Sum
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest = 0;
        int curr = 0;

        for(auto slope: gain){ 
            curr += slope;
            highest = max(highest, curr);
        } 

        return highest;

    }
};