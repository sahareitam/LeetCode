class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        int pos=0;
        for(auto command:commands){
            if(command == "RIGHT"){
                pos+=1;
            }else if(command == "LEFT"){
                pos-=1;
            }else if(command == "DOWN"){
                pos+= n;
            }else if(command == "UP"){
                pos-= n;
            }
        }
        return pos;
    }
};