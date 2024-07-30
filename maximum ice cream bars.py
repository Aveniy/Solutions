class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_bars = 0
        if costs[0] > coins:
            return 0
        

        for i in range(len(costs)):
            if costs[i] <= coins and coins >= 0:
                ice_bars += 1
                coins -= costs[i]
        return ice_bars
            

                 


            
        
