class Solution:
    def similarPairs(self, words: List[str]) -> int:

        
        wm = {}
        for word in words:
            current = sorted(set(word))
            current = ''.join(current)
            if current in wm:
                wm[current] += 1
            else:
                wm[current] = 1
        pairs = 0
        for word in wm:
            count = wm[word]
            pairs += (count*(count-1))//2
        return pairs





