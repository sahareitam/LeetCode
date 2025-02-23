class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            cur_sum = sqrt(x**2+y**2)
            if len(heap)<k:
                heapq.heappush(heap,(-1*cur_sum,point))
            else:
                cur_max = heapq.heappop(heap)
                if -1*cur_max[0] > cur_sum:
                    heapq.heappush(heap,(-cur_sum,point))
                else:
                    heapq.heappush(heap,cur_max)
        res = []
        for p in heap:
            res.append(p[1])
        return res