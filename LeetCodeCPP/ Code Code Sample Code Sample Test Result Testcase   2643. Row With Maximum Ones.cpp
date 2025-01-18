class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        vector<int> res = {0,0};
        int sum = 0;
        for(int row = 0;row<mat.size();row++)
        {
            sum = 0;
            for(int col = 0;col < mat[0].size();col++)
            {
                if(mat[row][col] == 1)
                {
                    sum++;
                }
            }
            if(sum > res[1])
            {
                res[0] = row;
                res[1] = sum;
            }
        }
        return res;
    }
};