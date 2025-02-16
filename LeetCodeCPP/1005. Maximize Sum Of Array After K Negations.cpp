class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int sum=0;
        int i=0;
        while(i<nums.size()&&nums[i]<0&&k>0){
            nums[i]*=-1;
            k--;
            i++;
        }

        if(k%2==1){
            sort(nums.begin(),nums.end());
            nums[0]*=-1;
        }


        for(auto num : nums){
            // cout<<num<<endl;
            sum+=num;
        }
        return sum;
    }
};