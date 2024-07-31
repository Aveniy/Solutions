class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles)-2
        summation = 0 
        while i < j:


            summation += piles[j]
            i += 1
            j -= 2
        return summation 
        
        
