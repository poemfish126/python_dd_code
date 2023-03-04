class MySegmentTreeNode:

    def __init__(self, start, end, val):
        self.start, self.end = start, end
        self.val = val
        self.left_child, self.right_child = None, None


class MySegmentTree:

    def __init__(self, start, end):
        self.root = self.build_tree(start, end)

    def build_tree(self, start, end):
        node = MySegmentTreeNode(start, end, -float('inf'))
        if start == end:
            return node

        node.left_child = self.build_tree(start, (start + end) // 2)
        node.right_child = self.build_tree((start + end) // 2 + 1, end)
        return node

    def insert(self, node, index, val):
        if node.start == index and node.end == index:
            node.val = val
            return
        if index <= node.left_child.end:
            self.insert(node.left_child, index, val)
        else:
            self.insert(node.right_child, index, val)
        node.val = max(node.left_child.val, node.right_child.val)

    def query(self, node, start, end):
        if end < start:
            return -float('inf')
        if node.start == start and node.end == end:
            return node.val
        if end <= node.left_child.end:
            return self.query(node.left_child, start, end)
        elif start >= node.right_child.start:
            return self.query(node.right_child, start, end)
        return max(
            self.query(node.left_child, start, node.left_child.end),
            self.query(node.right_child, node.right_child.start, end)
        )


class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """

    def shortest_subarray(self, A, K):
        prefix_sum = self.get_prefix_sum(A)
        sum2index = self.get_sum2index(prefix_sum, K)

        st = MySegmentTree(0, len(sum2index) - 1)
        answer = float('inf')
        for end in range(len(A)):
            st.insert(st.root, sum2index[prefix_sum[end]], end)
            start = st.query(st.root, st.root.start, sum2index[prefix_sum[end + 1] - K])
            if start != -float('inf'):
                answer = min(answer, end - start + 1)

        return answer if answer != float('inf') else -1

    def get_prefix_sum(self, A):
        prefix_sum = [0]
        for num in A:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum

    def get_sum2index(self, prefix_sum, K):
        prefix_sum_set = set()
        for num in prefix_sum:
            prefix_sum_set.add(num)
            prefix_sum_set.add(num - K)

        sum2index = {}
        for index, num in enumerate(sorted(list(prefix_sum_set))):
            sum2index[num] = index

        return sum2index


s = Solution()
nums = [2, 1, -1, 1, 2, -3]
k = 3
print(s.shortest_subarray(nums, k))
# 4   -2  3   -4  5   -6
# 0   1   2   3   4   5
# X   Y   X   Y   X   Y
# X   Y   Y   Y   Y   Y
