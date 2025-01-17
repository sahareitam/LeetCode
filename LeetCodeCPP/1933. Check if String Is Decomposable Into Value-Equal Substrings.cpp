class Solution {
public:
    bool isDecomposable(string s) {
        int len = 1;
        bool flag = true;
        for(int i=1;i<s.size();i++)
        {
            if(s[i] == s[i-1])
            {
                len++;
            }else
            {
                if((len-2) % 3 == 0 && flag)
                {
                    flag = false;
                    len = 1;
                }else if (len%3 == 0)
                {
                    len = 1;
                }else
                {
                    return false;
                }
            }if(i == s.size()-1 && flag && (len-2) % 3 == 0)
            {
                return true;
            }

        }
        return flag == false && (len%3 == 0);
    }
};