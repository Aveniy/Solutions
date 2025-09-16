class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse = True)
        arr = []

        while len(nums) > 0:
            minimum = nums.pop()    
            second_minimum = nums.pop() 

            arr.append(second_minimum)
            arr.append(minimum)

        return arr
