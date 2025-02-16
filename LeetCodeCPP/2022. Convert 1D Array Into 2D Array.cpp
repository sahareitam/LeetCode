class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        int len = original.size();
        if(len%n!=0 or len/n!=m){
            return {};
        }
        vector<vector<int>> res(m,vector<int>(n));
        for(int i=0;i<len;i++){
            res[i/n][i%n]=original[i];
        }
        return res;
    }
};