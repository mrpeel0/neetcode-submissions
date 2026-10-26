class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1

        while start <= end:
            m = start + ((end-start) // 2)
            if target > matrix[m][-1]:
                start = m + 1
           
            elif target < matrix[m][0]:
                end = m -1
        
            elif target <= matrix[m][-1] and target >= matrix[m][0]:
                
                l, r = 0, len(matrix[m]) -1
                while l <= r:
                    mid = l + ((r-l) // 2)
                    if target > matrix[m][mid]:
                        l = mid + 1
                    elif target < matrix[m][mid]:
                        r = mid -1
                    elif target == matrix[m][mid]:
                        return True
                return False
        return False
