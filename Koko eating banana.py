class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)
        ans = j
        while i <= j:
            mid = (i + j) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / mid)
            if hrs <= h:
                ans = min(ans, mid)
                j = mid - 1
            else:
                i = mid + 1
        return ans


            


        

           

            




         
        
        
