class Solution {
public:
    string findLongestWord(string s, vector<string>& dictionary) {
        sort(dictionary.begin(),dictionary.end(),[](string &a,string &b){
         if(a.size() != b.size()){
             return a.size() > b.size();
         }
         int i=0;
         while(i<a.size()){
             if(a[i]!=b[i]){
                 return a[i]< b[i];
             }
             i++;
         }
         return a<b;
        });

        for(int i=0;i<dictionary.size();i++){
            int count=0;
            for(int j=0;j<s.size();j++){
                if(s[j] == dictionary[i][count]){
                    count++;
                    if(count == dictionary[i].size()){
                        return dictionary[i];
                    }
                }
            }
        }
        return"";
    }
};