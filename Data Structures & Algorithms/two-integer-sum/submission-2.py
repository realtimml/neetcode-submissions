# from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            # if n in nums_map:
            #     continue

            nums_map[n] = i
        
        for i, n in enumerate(nums):
            if target - n not in nums_map or nums_map[target - n] == i:
                continue
            
            return [i, nums_map[target - n]]
