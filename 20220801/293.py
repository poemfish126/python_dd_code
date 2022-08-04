from typing import (
    List,
)


class Solution:
    """
    @param matrix: the matrix in problem
    @return: the depth of the tunnel.
    """

    def find_depth(self, matrix: List[List[int]]) -> int:
        #
        print(matrix)

        def contains_one(row):
            return 1 in row


        if not matrix:
            return 0
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if contains_one(matrix[mid]):
                start = mid + 1
            else:
                end = mid
        if contains_one(matrix[end]):
            return end
        if contains_one(matrix[start]):
            return start
        elif start > 1 and contains_one(matrix[start - 1]):
            return start - 1
        return 0





input = [[1, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 0, 1, 1],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0]]

input = [[1, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 1, 1, 1, 0, 0, 1],
         [1, 1, 1, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 1, 1, 1]]
input = [[1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1],
         [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1],
         [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1],
         [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1],
         [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
         [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
s = Solution()
print(s.find_depth(input))
