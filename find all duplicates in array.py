class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d, arr = set(), []
        for j in nums:
            if j in d:
                arr.append(j)
            else:
                d.add(j)
        return arr



       

        
