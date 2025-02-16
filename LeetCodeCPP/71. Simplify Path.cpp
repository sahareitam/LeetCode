class Solution {
public:
    string simplifyPath(string path) {
        int len = path.size();
        int i = len-1;
        string res = "";
        string word = "";
        stack<string> Mstack;
        stack<string> stack1;
        stack1.push("/");
        while(i>=1){
            if(path[i]=='/'){
                if(word.size()>0){
                    Mstack.push(word);
                }
                word = "";
            }else{
                word = path[i]+ word;
            }
            i--;
        }
        if(word.size()>0){
            Mstack.push(word);
        }
        while(Mstack.size() > 0){
            if(Mstack.top() == ".."){
                Mstack.pop();
                if(stack1.size()>1){
                    stack1.pop();
                }
            }else if(Mstack.top()=="."){
                Mstack.pop();
            }else{
                stack1.push(Mstack.top());
                Mstack.pop();
            }
        }
        while(stack1.size()>1){
            res = "/"+stack1.top() + res;
            stack1.pop();
        }
        if(res==""){
            res = "/";
        } 
        return res;   
    }
};