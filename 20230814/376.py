from typing import (
    List,
)
from lintcode.TreeNode import *


class Solution:
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        result = []
        path = []
        self.dfs(root, path, target, result, 0)
        return result

    def dfs(self, root: TreeNode, path: List[int], target: int, result: List[List[int]], total: int):
        if root is None:
            return
        path.append(root.val)
        total += root.val
        if root.left is None and root.right is None and total == target:
            result.append(path)
        self.dfs(root.left, path, target, result, total)
        self.dfs(root.right, path, target, result, total)
        path.pop()


s = Solution()
print(s.binary_tree_path_sum(node5492810, 11))
