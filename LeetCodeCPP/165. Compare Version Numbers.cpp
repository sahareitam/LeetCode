class Solution {
public:
    int compareVersion(string version1, string version2) {
        stringstream ss1(version1);
        stringstream ss2(version2);
        string s1;
        string s2;

        while(true){
            bool is_empty1 = !(!getline(ss1,s1,'.'));
            bool is_empty2 = !(!getline(ss2,s2,'.'));
            if(!is_empty1 && !is_empty2) break;
            if(!is_empty1) s1 = "";
            if(!is_empty2) s2 = "";
            int num1;
            int num2;
            if(s1.empty()){
                num1 = 0;
            }else{
                num1 = stoi(s1);
            }
            if(s2.empty()){
                num2 = 0;
            }else{
                num2 = stoi(s2);
            }
            cout<<num1<<" "<<num2<<endl;
            if(num1 < num2){
                return -1;
            }else if(num1 > num2){
                return 1;
            }
            s1=s2="";
        }
        return 0;
    }
};