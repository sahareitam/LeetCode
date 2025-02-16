class Solution {
public:
    string removeOccurrences(string s, string part) {
        int count=0;
        int i = 0;
        int p = 0;
        while(i<s.size()+1){
            if (p == part.size()){
                s.erase(i-p,p);
                i=0;
                p=0;
                continue;
            }else if(s[i] == part[p]){
                p++;
            }else{
                i=i-p;
                p = 0;
            }
            i++;
        }   
        return s;
    }
};