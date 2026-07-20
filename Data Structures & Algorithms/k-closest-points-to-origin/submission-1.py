class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for point in points:
            x , y = point[0], point[1]
            dist = x * x + y * y
            heapq.heappush(heap, (dist, x, y))

        res = []
        for i in range(k):
            dist, x , y = heapq.heappop(heap)
            res.append([x,y])

        return res