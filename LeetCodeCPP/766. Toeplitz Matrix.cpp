class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m =matrix.size();
        int n = matrix[0].size();
        for(int row=m-1;row>=0;row--){
            int nxt_row = row;
            for(int col=0;col<n-1;col++){
                if(nxt_row<m-1){
                    if(matrix[nxt_row][col] != matrix[nxt_row+1][col+1]){
                        return false;
                    }
                }
            }
        }
        return true;
    }
};