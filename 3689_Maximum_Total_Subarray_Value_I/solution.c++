// Approach: Greedy
class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int minimum = INT_MAX, maximum = INT_MIN; 
        for(int x: nums){ 
            minimum = min(minimum, x); 
            maximum = max(maximum, x);
        }

        return (long long) (maximum - minimum) * k;
    }
};