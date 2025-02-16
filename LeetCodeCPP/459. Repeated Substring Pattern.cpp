class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for(int i=1;i<n/2+1;i++){
            if(n%i==0){
                string sub = s.substr(0,i);
                string checker = "";
                for(int j=0;j<n/i;j++){
                    checker+=sub;
                }
                if(checker == s){
                    return true;
                }
            }
        }
        return false;
    }
};