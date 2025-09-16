class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(set)
        
        for i in range(0,len(rings), 2):
            out = rings [i: i+2]
            d[out[1]].add(out[0])
        count = 0
        for i , j in d.items():
            if len(j) == 3:
                count +=1
        return count
