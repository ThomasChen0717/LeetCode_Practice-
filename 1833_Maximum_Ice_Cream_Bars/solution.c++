// Approach: Counting Sort
class Solution {
private: 
    vector<int> coutingSort(vector<int>& costs, int limit) {
        vector<int> res(limit + 1);

        for(auto cost : costs){
            if(cost <= limit){
                res[cost] += 1; 
            }
        }

        return res;
    }
public:
    int maxIceCream(vector<int>& costs, int coins) {
        vector<int> sorted = coutingSort(costs, coins);

        int cnt = 0;
        int currentCoins = coins;

        for(int i = 1; i <= coins; i++){ 
            if(currentCoins < i){ 
                break;
            }
            int canBuy = min(sorted[i], currentCoins / i);

            cnt += canBuy;
            currentCoins -= canBuy * i;
        }

        return cnt;
    }
};