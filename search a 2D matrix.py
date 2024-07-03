class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) -1
        while start <= end:
            mid = (start + end) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                end = mid - 1
        i = 0
        new_matrix = matrix[mid]
        n = len(new_matrix) - 1
        while i <= n:
            mid = (i + n) //2
            if target == new_matrix[mid]:
                return True
            elif target > new_matrix[mid]:
                i = mid + 1
            else:
                n = mid - 1
        return False



        
