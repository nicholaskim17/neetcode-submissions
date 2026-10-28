class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #index: number, value: index
        hm = {}

        for i in range(len(nums)):

            find = target - nums[i]

            if find in hm:
                return([hm[find],i])
            else:
                hm[nums[i]] = i

