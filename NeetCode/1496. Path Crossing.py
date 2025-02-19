class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        cur = [0,0]
        points = {"0,0":0}
        for d in path:
            if d == "N":
                cur[1]+=1
            elif d == "S":
                cur[1]-=1
            elif d == "E":
                cur[0]+=1
            elif d == "W":
                cur[0]-=1
            key = str(cur[0]) + ',' + str(cur[1])
            if key not in points:
                points[key] = 0
            else:
                return True
        return False
