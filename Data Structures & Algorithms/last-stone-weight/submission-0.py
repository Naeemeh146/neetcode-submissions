import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if stones:
            heaped = [-stone for stone in stones]
            heapq.heapify(heaped)

            while len(heaped) > 1:

                x = heapq.heappop(heaped)
                y = heapq.heappop(heaped)

                if x != y:
                    val = x - y
                    heapq.heappush(heaped, val)

            return -heaped[0] if heaped else 0

        return 0