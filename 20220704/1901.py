import sys
from typing import (
    List,
)


class Solution:
    """
    @param a: The array A.
    @return: The array of the squares.
    """

    def square_array(self, a: List[int]) -> List[int]:
        i, j, output = 0, len(a) - 1, [0] * len(a)

        while i <= j:
            aa, b = a[i] ** 2, a[j] ** 2
            output[j - i] = max(aa, b)
            i, j = i + (aa > b), j - (not aa > b)

        print(output)
        return output

        # write your code here
        # result = []
        # zero, position, left, right = -1, 0, -1, -1
        # zero_distince = sys.maxsize
        # for i in a:
        #     if abs(i) < zero_distince:
        #         zero_distince = abs(i)
        #     else:
        #         left, right = position - 1, position - 1
        #         break
        #     position = position + 1
        # while left >= 0 or right < len(a):
        #     if left == right:
        #         result.append(zero_distince * zero_distince)
        #         left = left - 1
        #         right = right + 1
        #     if left >= 0 and abs(a[left]) < abs(a[right]):
        #         result.append(a[left] * a[left])
        #         left = left - 1
        #         continue
        #     if right < len(a) and abs(a[left]) >= abs(a[right]):
        #         result.append(a[right] * a[right])
        #         right = right + 1
        #         continue
        # print(result)
        # return result



a = [-4, -1, 0, 3, 10]
b = [-9685,-8029,-449,536,579,1595,2914,3111,3126,4770,6323,6961,7038,7306,8232,9368,9433]
s = Solution()
s.square_array(b)
