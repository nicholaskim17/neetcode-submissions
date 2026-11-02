class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            target = nums[i]
            l = i + 1
            r = len(nums) - 1

            if i!=0 and nums[i] == nums[i-1]:
                continue

            while l<r:

                if nums[l] + nums[r] + target > 0:
                    r-=1
                elif nums[l] + nums[r] + target < 0:
                    l+=1
                else:
                    output.append([nums[i], nums[l], nums[r]])

                    l+=1
                    r-=1

                    if l>=r:
                        break

                    while nums[l] == nums[l-1]:
                        l+=1

                        if l>=r:
                            break
                    while nums[r] == nums[r+1]:
                        r-=1

                        if l>=r:
                            break
                        



        return output

        