class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans, cnt = 0, 0
        for i in range(len(flips)):
            cnt = max(cnt, flips[i])
            if cnt == i + 1:
                ans += 1
        return ans




        
