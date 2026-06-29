import math as m 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zero_count = nums.count(0)

        if zero_count > 1 :
            return [0] * len(nums)
        if zero_count == 1 :
            product = 1 
            for num in nums: 
                if num != 0:
                    product *= num
            for num in nums:
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            return output 
        product = m.prod(nums)
        for num in nums:
            output.append(product//num)
        return output
            

            
            
            