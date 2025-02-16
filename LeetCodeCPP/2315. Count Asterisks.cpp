class Solution {
public:
    int countAsterisks(string s) {
        int sum=0;
        int count=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='|'&& count<2){
                count++;
                if(count==2){
                    count = 0;
                }
            }
            else if(count == 0 && s[i]=='*'){
                sum++;
            }
        }
        return sum;
    }
};