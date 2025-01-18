class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_set<char> set;
        for(char c : s)
        {
            if(set.find(c) != set.end())
            {
                return c;
            }else
            {
                set.insert(c);
            }
        }
        return ' ';
    }
};