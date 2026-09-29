from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = defaultdict(int)

        for n in nums:
            nums_count[n] += 1
            
            if nums_count[n] > 1:
                return True
        
        return False