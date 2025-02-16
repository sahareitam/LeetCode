class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int res = 0;
        sort(points.begin(),points.end(),[](vector<int>&a, vector<int>&b){
            if (a[0] != b[0]){
                return a[0] < b[0];
            }
            return a[1] > b[1];
        });

        for(int p1=0;p1<points.size();p1++){
            int between = -1;
            for(int p2=p1+1;p2<points.size();p2++){
                if(points[p1][1]>=points[p2][1] && between <points[p2][1]){
                    res++;
                    if(between < points[p2][1]){
                        between = points[p2][1];
                    }
                }
            }
        }
        return res;
    }
};