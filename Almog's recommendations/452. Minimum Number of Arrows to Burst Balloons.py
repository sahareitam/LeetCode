class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for i in range(1, len(points)):
            if end < points[i][0]:
                arrows += 1
                end = points[i][1]

        return arrows





