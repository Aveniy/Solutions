class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])

        for i in range(n):
            for j in  range(i+1,n):
                if nums[i]+nums[j] > nums[j]+nums[i]:
                    continue
                else:
                    nums[i],nums[j] = nums[j],nums[i]
            res = "".join(nums)
        if int(res) == 0:
            return "0"
        return res
        
        
