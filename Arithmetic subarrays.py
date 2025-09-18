class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [True] * len(l)
        
        for num in range(len(l)):
            sub = nums[ l[num] : r[num] + 1]
            sub.sort()
            
            
            diff = sub[1] - sub[0]
            for i in range(1, len(sub)):
                if sub[i] - diff == sub[i - 1]:
                    continue
                    
                    
                else:
                    res[num] = False 
                    break      
            
        return res




        
