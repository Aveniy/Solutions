class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        d = {' ' : ' '}
        ans = []
        a = 'abcdefghijklmnopqrstuvwxyz'
        j = 0
        for i in range(len(key)):
            if key[i] not in d:
                d[key[i]] = a[j]
                j += 1
        for c in message:
            if c in d:
                ans.append(d[c])
            else:
                continue
        return ''.join(ans)
        
        
        
