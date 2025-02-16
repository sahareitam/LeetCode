class Solution {
public:
    string getSmallestString(string s) {
        for(int i=1;i<s.size();i++){
            if((s[i]+s[i-1])%2==0 && s[i]< s[i-1]){
                char temp = s[i-1];
                s[i-1] = s[i];
                s[i]=temp;
                break;
            }   
        }
        return s;
    }
};