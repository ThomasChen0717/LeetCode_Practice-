// Approach 1: Backtracking
class Solution {
private: 
    bool valid(const string& s, int start, int length) {
        return length == 1 || (s[start] != '0' && (length < 3 || s.substr(start, length) <= "255")); 
    }

    void helper(const string& s, int start, vector<int>& dots, vector<string>& res){ 
        const int remainingLength = s.length() - start; 
        const int remainingIntegers = 4 - dots.size();

        if (remainingLength > remainingIntegers * 3 || remainingLength < remainingIntegers){
            return;
        }

        if (dots.size() == 3) {
            if (valid(s, start, remainingLength)) { 
                string temp; 
                int last = 0; 
                for(int dot : dots){
                    temp.append(s.substr(last, dot));
                    last += dot; 
                    temp.append(".");
                }
                temp.append(s.substr(start)); 
                res.push_back(temp);
            }
            return;
        }

        for (int curPos = 1; curPos <= 3 && curPos <= remainingLength; curPos++){
            dots.push_back(curPos);

            if(valid(s, start, curPos)){
                helper(s, start + curPos, dots, res);
            }

            dots.pop_back();
        }
    }
public:
    vector<string> restoreIpAddresses(string s) {
        if(s.size() > 12){
            return {};
        }

        vector<int> dots; 
        vector<string> res; 

        helper(s, 0, dots, res);

        return res;

    }
};

// Approach 2: Iteration
class Solution {
    bool valid(const string& s, int start, int length) {
        return length == 1 ||
               (s[start] != '0' &&
                (length < 3 || s.substr(start, length) <= "255"));
    }

public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        int length = s.length();
        for (int len1 = max(1, length - 9); len1 <= 3 && len1 <= length - 3;
             ++len1) {
            if (!valid(s, 0, len1)) {
                continue;
            }
            for (int len2 = max(1, length - len1 - 6);
                 len2 <= 3 && len2 <= length - len1 - 2; ++len2) {
                if (!valid(s, len1, len2)) {
                    continue;
                }
                for (int len3 = max(1, length - len1 - len2 - 3);
                     len3 <= 3 && len3 <= length - len1 - len2 - 1; ++len3) {
                    if (valid(s, len1 + len2, len3) &&
                        valid(s, len1 + len2 + len3,
                              length - len1 - len2 - len3)) {
                        ans.push_back(s.substr(0, len1) + "." +
                                      s.substr(len1, len2) + "." +
                                      s.substr(len1 + len2, len3) + "." +
                                      s.substr(len1 + len2 + len3));
                    }
                }
            }
        }
        return ans;
    }
};