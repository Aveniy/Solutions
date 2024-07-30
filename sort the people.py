class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new_list = []
        new_height = sorted(heights, reverse=True)

        for i in range(len(heights)+1):
            new_list.append(names[heights.index(heights[i])])
        return new_list

        
        
         






        
                   



        
