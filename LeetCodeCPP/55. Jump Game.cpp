class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        int index = len-1;
        for(int i=len-2;i>=0;i--){
            if(nums[i]+i>=index){
                index=i;
            }
        }
        return index == 0;
    }
};