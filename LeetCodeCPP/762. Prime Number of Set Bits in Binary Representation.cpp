class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        int res = 0;
        for(int i=left;i<=right;i++){
            int count = 0;
            int x=i;
            while(x>0){
                count += x%2;
                x=x/2;
            }
            cout<<count<<endl;
            if(count==2||count==3||count==5||count==7||count==11||count==13||count==17||count==19){
                res+=1;
            }
        }
        return res;
    }
};