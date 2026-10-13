class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        left = 0
        right = total-1
        while left <= right:
            mid = (left+right)//2
            row = mid//cols
            col = mid%cols

            value = matrix[row][col]
            if value==target:
                return True
            elif value < target:
                left = mid+1
            else:
                right = mid-1

        return False
