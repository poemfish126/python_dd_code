from typing import (
    List,
)


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        # start + 1 < end
        # start + (end - start) / 2
        # A[mid] ==, <, > A[start]
        # A[end] ? target
        result = False
        if not matrix:
            return result

        # n * m matrix, 1 - n * m numbers
        # e.g. 20 * 5 = 100, so No. 50 =  col * 2 + 10
        col = len(matrix[0])
        start, end = 0, len(matrix) * col - 1

        while start + 1 < end:
            mid = (start + end) // 2
            value = matrix[mid // col][mid % col]
            if value > target:
                end = mid
            elif value < target:
                start = mid + 1
            else:
                return True

        if matrix[end // col][end % col] == target:
            return True
        elif matrix[end // col][end % col] > target:
            if end % col - 1 >= 0:
                return matrix[end // col][end % col - 1] == target
            else:
                return matrix[end // col - 1][end - 1] == target
        return result


matrix = [[1, 4, 5], [6, 7, 8]]
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

target = 7
s = Solution()
print(s.search_matrix(matrix, target))
