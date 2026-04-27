class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}
        for i in range(len(nums)):

            # Firs calculate complement
            res = target - nums[i]

            if res in map_dict:
                return [map_dict[res] , i]

            # Store current index and value for checking
            map_dict[nums[i]] = i
        
        
        return 
            




        