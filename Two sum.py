class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i, num in enumerate(nums):
            if  target - num in d and i != d[target-num]:
                return [i, d[target-num]]           

            

            
