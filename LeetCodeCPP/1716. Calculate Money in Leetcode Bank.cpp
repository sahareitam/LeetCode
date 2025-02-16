class Solution {
public:
    int totalMoney(int n) {
        int weeks = n/7;
        int last_week = n%7;
        return weeks*21+(weeks*(weeks+1)/2)*7+weeks*last_week+(last_week*(last_week+1))/2;
    }
};