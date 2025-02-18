class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        dic = {}
        for city in paths:
            dic[city[0]] = city[1]

        city1 = paths[0][0]

        while city1 in dic:
            city1 = dic[city1]

        return city1