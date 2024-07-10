class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = -1
        
        for i in range(n-1,-1,-1):
            max_val = max(result,arr[i])
            
            arr[i] = result      
           
            result = max_val
        return arr




        
        
        
        
        
