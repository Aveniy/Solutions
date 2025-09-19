class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []
        
        for i in range(n):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                pre_index = stack.pop()
                res[pre_index] = i - pre_index
            stack.append(i)
        return res




            
            


        
