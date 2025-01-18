class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.rbegin(),cost.rend());
        int count = 0;
        int sum = 0;
        for(int i = 0;i < cost.size();i++)
        {
            count ++;
            if (count == 3)
            {
                count = 0;
            }else
            {
                sum += cost[i];
            }
        }
        return sum;
    }
};