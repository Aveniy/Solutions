class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        pt = []
        for i in points:
            pt.append(i[0])
        pt.sort()
        diff = 0
        for i in range(len(pt)-1):
            diff = max(diff, pt[i]- pt[i-1])
        return diff



    
        
