class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 0
        j = 1
        while i < n and j < n:
            if nums[i] == nums[j]:
                nums[i] = 2*nums[i]
                nums[j] = 0
                i += 1
                j += 1
            i+=1
            j += 1
        k = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1 
        return nums




        
