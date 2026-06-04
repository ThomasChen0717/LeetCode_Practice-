// Approach: Binary Search 
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1; 

        while(left <= right){ 
            int mid = left + (right - left) / 2; 
            if(nums[mid] == target) return true; 
            else if(nums[mid] > nums[left]){ 
                if(target >= nums[left] && nums[mid] > target){ 
                    right = mid - 1; 
                }
                else{ 
                    left = mid + 1;
                }
            } else if(nums[mid] < nums[left]){ 
                if(target > nums[mid] && nums[right] >= target){ 
                    left = mid + 1; 
                }
                else{ 
                    right = mid - 1;
                }
            } else{
                left += 1;
            }
        }

        return false;
    }
};