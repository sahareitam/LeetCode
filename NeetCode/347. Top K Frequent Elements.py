class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        for val, count in Counter(nums).items():
            if len(heap) < k:
                heapq.heappush(heap, (count, val))
            else:
                heapq.heappushpop(heap, (count, val))
        for i in range(k):
            res.append(heap[i][1])

        return res
