class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            cov = False
            for start, end in ranges:
                if start <= num <= end:
                    cov = True
                    break
                
            if not cov:return False
        return True
        
        

            


            
            





        
        
        
                 

        
        
        
        

        



         





        



        
