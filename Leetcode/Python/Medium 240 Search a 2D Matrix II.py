class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return True in [target in row for row in matrix]