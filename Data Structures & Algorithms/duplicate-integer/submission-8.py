class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for ind, val in enumerate(nums):
            if val in s:
                return True 
            else:
                s.add(val)

        return False
        
        