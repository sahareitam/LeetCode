class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> people(num_people);
        int x=1;
        int i=0;
        while(candies>x){
            if(i<num_people){
                people[i]+=x;
                candies-=x;
                x++;
            }else{
                i= -1;
            }
            i++;
        }
        if(i<num_people){
            people[i]+=candies;
        }else{
            people[0]+=candies;
        }
        return people;
    }
};