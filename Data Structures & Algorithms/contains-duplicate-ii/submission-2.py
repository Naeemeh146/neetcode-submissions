class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited_dict = {}

        for i , num in enumerate(nums):
            
            if num in visited_dict:
                value = i - visited_dict[num]
                if value <= k:
                    return True


            visited_dict[num] = i


        return False