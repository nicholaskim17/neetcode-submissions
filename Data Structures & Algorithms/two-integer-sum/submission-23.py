class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} #ind: number, value: index

        for ind, val in enumerate(nums):
            tar = target - val
            if tar in hm:
                return ([hm[tar], ind])
            hm[val] = ind
        