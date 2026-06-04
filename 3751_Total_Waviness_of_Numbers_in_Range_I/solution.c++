// Approach 1: Enumeration
class Solution {
private: 
    int waviness(int num) { 
        int res = 0;

        int right = num % 10;
        num /= 10;
        while(num >= 10){ 
            int left = (num / 10) % 10; 
            int curr = num % 10; 
            if((curr > left && curr > right) || 
                (curr < left && curr < right)){ 
                res ++;
            }
            num /= 10;
            right = curr;
        }

        return res;
    }     
public:
    int totalWaviness(int num1, int num2) {
        int total = 0;
        for(int i = num1; i <= num2; i++){
            total += waviness(i);
        }
        return total;
    }
};

// Approach 2: Dynamic Programming
class Solution {
private:
    struct State {
        long long count; // number of valid numbers from this state
        long long sum;   // total waviness from this state
    };

    string s;

    // pos: current digit index
    // prev2: digit two positions back, 10 means "none"
    // prev1: previous digit, 10 means "none"
    // started: whether number has started
    // We usually do NOT memoize tight = true states
    State memo[20][11][11][2];
    bool seen[20][11][11][2];

    State dfs(int pos, int prev2, int prev, bool tight, bool started){
        if(pos == s.size()){ 
            return {1, 0};
        }

        if (!tight && seen[pos][prev2][prev][started]) {
            return memo[pos][prev2][prev][started];
        }

        int limit = tight ? s[pos] - '0' : 9;

        State ans = {0, 0};

        for (int d = 0; d <= limit; d++) {
            bool newTight = tight && (d == limit);

            if (!started && d == 0) {
                State child = dfs(pos + 1, 10, 10, newTight, false);
                ans.count += child.count;
                ans.sum += child.sum;
                continue;
            }

            int add = 0;

            if (started && prev2 != 10 && prev != 10) {
                if ((prev > prev2 && prev > d) ||
                    (prev < prev2 && prev < d)) {
                    add = 1;
                }
            }

            int newPrev2;
            int newPrev;

            if (!started) {
                newPrev2 = 10;
                newPrev = d;
            } else {
                newPrev2 = prev;
                newPrev = d;
            }
            
            State child = dfs(pos + 1, newPrev2, newPrev, newTight, true);

            ans.count += child.count;
            ans.sum += child.sum + add * child.count;
        }

        if (!tight) {
            seen[pos][prev2][prev][started] = true;
            memo[pos][prev2][prev][started] = ans;
        }

        return ans;
    }

    long calc(int n) {
        if (n <= 0) return 0;

        s = to_string(n);

        memset(seen, false, sizeof(seen));

        State ans = dfs(0, 10, 10, true, false);

        return ans.sum;
    }

public:
    int totalWaviness(int num1, int num2) {
        return calc(num2) - calc(num1 - 1);
    }
};