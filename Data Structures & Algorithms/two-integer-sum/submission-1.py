from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = defaultdict()

        for i , num in enumerate(nums):

            complete = target - num


            if num in map_dict:
                return [map_dict[num], i]

            map_dict[complete] = i


        