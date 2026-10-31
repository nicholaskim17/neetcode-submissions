class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zero_ctr = 0
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_ctr+=1
            else:
                product *= nums[i]

        
        if zero_ctr == 0:
            for i in range(len(nums)):
                output.append(product//nums[i])

        if zero_ctr == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(product)
                else:
                    output.append(0)
        if zero_ctr>1:
            for i in range(len(nums)):
                output.append(0)

        return output



        