from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_dict = Counter(tasks)
        heap = [-freq for freq in task_dict.values()]

        heapq.heapify(heap)

        queue = deque()
        time = 0
        while heap or queue:
            
            time += 1

            if heap:
                fetch = heapq.heappop(heap) + 1
                if fetch != 0:
                    queue.append((fetch, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time