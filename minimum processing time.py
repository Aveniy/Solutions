class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        
        i = len(tasks) - 1
        t = 0
        count = 0
        
        while i > 0 and t < len(processorTime):
            count = max(count, processorTime[t] + tasks[i])
            i -= 4
            t+=1
                
                
        return count







         
        
