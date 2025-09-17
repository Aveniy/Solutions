class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        
        if num % 3 == 0:
            y = int(num / 3)
            return [y-1, y, y+1]




                
        
        
