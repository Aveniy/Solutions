class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if '..' in log:
                count -= count > 0
            elif '.' in log:
                continue
            else:
                count+=1
        return count if count > 0 else 0


        
