from typing import (
    List,
)


class Solution:

    def contains_nearby_duplicate1(self, nums: List[int], k: int) -> bool:

        if not nums or k < 1 or len(nums) < k:
            return False
        array = []
        for i in range(len(nums)):
            array.append((nums[i], i))
        sorted_array = sorted(array)
        current = sorted_array[0][0]
        base_index = sorted_array[0][1]
        index = 1
        while index < len(nums):
            if sorted_array[index][0] == current and sorted_array[index][1] - base_index == k:
                return True
            if sorted_array[index][0] != current:
                current = sorted_array[index][0]
                base_index = sorted_array[index][1]
            if sorted_array[index][1] - base_index > k:
                base_index = sorted_array[index][1]

        return False


    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for index, value in enumerate(nums):
            if value in dic and index - dic[value] <= k:
                return True
            dic[value] = index
        return False


s = Solution()
# print(s.contains_nearby_duplicate([1, 2, 1], 0))
# print(s.contains_nearby_duplicate([1, 2, 1], 2))
print(s.contains_nearby_duplicate([1, 2, 1, 1], 3))
