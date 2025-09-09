class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1 :
            return [-1]
        for i in range(len(arr)):
            max_val = 0
            if i == len(arr)-1:
                arr[i] = -1
                
            for j in range(len(arr)-1, i, -1):
                max_val = max(max_val, arr[j])
                arr[i] = max_val
        return arr




        
        
        
        
        
