class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new_mat = []
        len_mat = []
        for row in mat:
            for num in row:
                new_mat.append(num)

        if r*c != len(new_mat):
            return mat
        else:
            for row_inx in range(r):
                len_mat.append(new_mat[row_inx * c : row_inx * c + c])
            return len_mat

        

        

        
         
        
        
