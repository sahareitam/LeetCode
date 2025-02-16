class Solution {
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        map<int,int> map;
        for(vector<int> item : items1){
            if (map.count(item[0]) == 0){
                map[item[0]]=item[1];
            }else{
                map[item[0]]+=item[1];
            }
        }
        for(vector<int> item : items2){
            if (map.count(item[0]) == 0){
                map[item[0]]=item[1];
            }else{
                map[item[0]]+=item[1];
            }
        }
        vector<vector<int>> ret;
        for(auto [v,w] : map){
            ret.push_back({v,w});
        }
        return ret;
    }
};