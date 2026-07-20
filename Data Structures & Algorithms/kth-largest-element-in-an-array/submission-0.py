class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums:
            nums = [-num for num in nums]
            heapq.heapify(nums)


            for i in range(k):

                if i == k-1:
                    return  - heapq.heappop(nums)

                heapq.heappop(nums)

        