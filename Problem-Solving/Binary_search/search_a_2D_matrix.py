class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        s = 0
        e = (row*col)-1
        while s<=e :
            mid = (s+e)//2 
            i = mid // col
            j = mid % col
            if matrix[i][j] == target :
                return True
            elif matrix[i][j] < target :
                s = mid + 1
            elif matrix[i][j] > target :
                e = mid - 1
        return False