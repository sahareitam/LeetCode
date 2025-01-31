class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dic = {}
        for e in emails:
            user = e[:e.index('@')]
            if '.' in user:
                user = user.replace('.', '')
            if '+' in user:
                dic[user[:user.index('+')]+e[e.index('@'):]] = 0
            else:
                dic[user+e[e.index('@'):]] = 0
        return len(dic)