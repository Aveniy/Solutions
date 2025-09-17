class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr =[1]
        for num in range(2, n+1):
            if n % num == 0:
                arr.append(num)
        return -1 if k > len(arr) else arr[k-1]

        
