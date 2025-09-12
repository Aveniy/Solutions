class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        moves = 0
        remaining_water = capacity
        for i, x in enumerate(plants):
            if remaining_water < x:
                moves += 2 * i
                remaining_water = capacity
            moves += 1
            remaining_water -= x
        return moves 


        
