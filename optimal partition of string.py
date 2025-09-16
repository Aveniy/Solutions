class Solution:
    def partitionString(self, s: str) -> int:
        cont = set()
        count = 1
        for i in range(len(s)):
            if s[i] not in cont:
                cont.add(s[i])
            elif s[i] in cont:
                cont.clear()
                cont.add(s[i])
                count+=1
        return count 
