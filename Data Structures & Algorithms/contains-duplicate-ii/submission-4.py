class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        visited_window = set()
        l = 0

        for r in range(len(nums)):

            if r - l > k:
                visited_window.remove(nums[l])
                l += 1 

            if nums[r] in visited_window:
                return True
            
            visited_window.add(nums[r])


        return False