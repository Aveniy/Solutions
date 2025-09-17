class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = 1
        sufProduct = 1
        product = [0] * len(nums)
        for i in range(len(nums)):
            product[i] = preProduct
            preProduct *= nums[i]
            
        
        for i in range(len(nums)-1, -1, -1):
            product[i] *= sufProduct

            sufProduct *= nums[i]
            
        
        
        return product
        
        


        
           




        
